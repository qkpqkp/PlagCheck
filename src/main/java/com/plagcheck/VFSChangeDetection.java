package com.plagcheck;
import com.intellij.openapi.actionSystem.AnAction;
import com.intellij.openapi.actionSystem.AnActionEvent;
import com.intellij.openapi.application.Application;
import com.intellij.openapi.application.ApplicationManager;
import com.intellij.openapi.editor.Document;
import com.intellij.openapi.editor.Editor;
import com.intellij.openapi.fileEditor.FileEditorManager;
import com.intellij.openapi.project.Project;
import com.intellij.openapi.ui.popup.JBPopupFactory;
import com.intellij.openapi.vfs.LocalFileSystem;
import com.intellij.openapi.vfs.VirtualFile;
import com.intellij.openapi.vfs.VirtualFileManager;
import com.intellij.openapi.vfs.newvfs.BulkFileListener;
import com.intellij.openapi.vfs.newvfs.events.VFileContentChangeEvent;
import com.intellij.openapi.vfs.newvfs.events.VFileEvent;
import org.jetbrains.annotations.NotNull;
import org.json.JSONArray;
import org.json.JSONObject;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import javax.swing.*;
import java.io.*;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class VFSChangeDetection extends AnAction {
    private Map<String,String> retrieve2(String src){
        Map<String, String> CodeMap = new HashMap<>();
        String key = "AIzaSyB-UHIT2lz1Hw-XyeFAQ7dJW67mNWCDnKg";
        String cx = "007835117730733246990:1ek1-aykdo4";
        String search_url = "https://www.googleapis.com/customsearch/v1?key=" + key + "&cx=" + cx + "&q=" + URLEncoder.encode(src, StandardCharsets.UTF_8);
        String json;
        try {
            json = Jsoup.connect(search_url).ignoreContentType(true).execute().body();
        }catch (IOException e){
            return null;
        }
        JSONObject obj = new JSONObject(json);
        JSONArray items = obj.getJSONArray("items");
        int count = 0;
        for (int i = 0; i < items.length(); i++) {
            if (count > 10) {
                break;
            }
            JSONObject item = items.getJSONObject(i);
            String link = item.getString("link");
            if (CodeMap.keySet().contains(link)) {
                continue;
            }
            if (link.startsWith("https://github.com/") && link.endsWith(".py")) {
                org.jsoup.nodes.Document doc;
                String raw_link = "";
                try {
                    doc = Jsoup.connect(link).get();
                } catch (IOException e) {
                    continue;
                }
                Element element = doc.getElementById("raw-url");
                raw_link = "https://github.com"+element.attr("href");

                try {
                    doc = Jsoup.connect(raw_link).get();
                } catch (IOException e) {
                    continue;
                }
                String code = doc.wholeText();
                CodeMap.put(link, code);
                count++;
            }
        }
        return CodeMap;
    }
    private Map<String,String> retrieve(String src){
        Map<String, String> CodeMap = new HashMap<>();
        String key = "AIzaSyB-UHIT2lz1Hw-XyeFAQ7dJW67mNWCDnKg";
        String cx = "007835117730733246990:1ek1-aykdo4";
        String[] queries = src.split("\\r?\\n");
        for(String query:queries) {
            String search_url = "https://www.googleapis.com/customsearch/v1?key=" + key + "&cx=" + cx + "&q=" + query;
            String json;
            try {
                json = Jsoup.connect(search_url).ignoreContentType(true).execute().body();
            }catch (IOException e){
                continue;
            }
            JSONObject obj = new JSONObject(json);
            JSONArray items = obj.getJSONArray("items");
            int count = 0;
            for (int i = 0; i < items.length(); i++) {
                if(count>2){
                    break;
                }
                JSONObject item = items.getJSONObject(i);
                String link = item.getString("link");
                if(CodeMap.keySet().contains(link)){
                    continue;
                }
                if (link.startsWith("https://stackoverflow.com/questions/")) {
                    /*
                    org.jsoup.nodes.Document doc;
                    try {
                        doc = Jsoup.connect(link).get();
                    }catch (IOException e){
                        continue;
                    }
                    Elements elements = doc.getElementsByClass("code");

                    List<String> codes = new ArrayList<String>();
                    for (Element e : elements) {
                        if(e.parent().tagName()!="pre"){
                            continue;
                        }
                        codes.add(e.text());
                    }
                    CodeMap.put(link, codes);
                    */

                } else if (link.startsWith("https://github.com/") && link.endsWith(".py")) {
                    org.jsoup.nodes.Document doc;
                    try {
                        doc = Jsoup.connect(link).get();
                    }catch (IOException e){
                        continue;
                    }
                    Elements elements = doc.getElementsByTag("tr");
                    String code = "";
                    for (Element e : elements) {
                        code += e.text();
                        code += '\n';
                    }
                    CodeMap.put(link, code);
                    count++;
                }
            }
        }
        return CodeMap;
    }

    private String checkPlag(String link, String src_code,String susp_code) throws FileNotFoundException {
        Runtime r = Runtime.getRuntime();
        String [] cmd = new String[2];
        cmd[0] = "python";
        //Should change to relative path
        cmd[1] = "C:\\Users\\Doly\\PlagCheck\\src\\main\\resources\\PlagCheck1.0.py";
        PrintWriter out1 = new PrintWriter("C:\\Users\\Doly\\PlagCheck\\src\\main\\resources\\code1.py");
        out1.print(susp_code);
        out1.close();
        PrintWriter out2 = new PrintWriter("C:\\Users\\Doly\\PlagCheck\\src\\main\\resources\\code2.py");
        out2.print(src_code);
        out2.close();
        String s = "";
        String resultString = "";
        try {
            Process p = r.exec(cmd);
            BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));

            while((s=in.readLine()) != null){
                resultString=resultString.concat(s);
            }
            /*
            BufferedReader err = new BufferedReader(new InputStreamReader(p.getErrorStream()));
            while((s=err.readLine()) != null){
                System.out.println(s);
            }*/
        } catch (IOException e) {
            e.printStackTrace();
        }
        return resultString;
    }
    private Map<Integer, List<Integer>> parseResult(String resultString){
        try {
            resultString = resultString.replaceAll("\\s", "");
            resultString = resultString.replaceAll("\\[", "");
            resultString = resultString.replaceAll("}", "");
            resultString = resultString.replaceAll("\\{", "");
            Map<Integer, List<Integer>> result = new HashMap<>();
            String[] resultSplit = resultString.split("],");
            for (String s : resultSplit) {
                s = s.replaceAll("]", "");
                String[] Mapping = s.split(":");
                List<Integer> tempList = new ArrayList<>();
                String[] tempSplit = Mapping[1].split(",");
                for (String t : tempSplit) {
                    tempList.add(Integer.parseInt(t));
                }
                result.put(Integer.parseInt(Mapping[0]), tempList);
            }
            return result;
        }catch(Exception e){
            return null;
        }
    }
    @Override
    public void actionPerformed(@NotNull AnActionEvent e){

        Application app = ApplicationManager.getApplication();
        app.getMessageBus().connect(app).subscribe(VirtualFileManager.VFS_CHANGES, new BulkFileListener() {
            @Override
            public void after(@NotNull List<? extends VFileEvent> events) {
                for(VFileEvent event:events){
                    if (event.getFileSystem() instanceof LocalFileSystem && event instanceof VFileContentChangeEvent) {
                        VirtualFile vfile = event.getFile();
                        Map<String, String> CodeMap;
                        Editor editor = FileEditorManager.getInstance(e.getProject()).getSelectedTextEditor();
                        Project project = e.getProject();
                        Document currentdoc = editor.getDocument();
                        String src = currentdoc.getText(); //Saved Codes
                        CodeMap = retrieve2(src);
                        System.out.println(CodeMap.keySet().size());
                        for(String s:CodeMap.keySet()) {
                            Map<Integer, List<Integer>> result = new HashMap<>();
                            try {
                                String resultString = checkPlag(s, CodeMap.get(s),src);
                                System.out.println(resultString);
                                result = parseResult(resultString);
                                if(result==null){
                                    continue;
                                }
                            } catch (FileNotFoundException fileNotFoundException) {
                                fileNotFoundException.printStackTrace();
                            }
                            if ((double)result.keySet().size() / currentdoc.getLineCount() > 0.5) {
                                System.out.println(s);
                            }
                        }
                        JTextField text = new JTextField("Here I am", 20);
                        JComponent panel = new JPanel();
                        panel.setSize(40,20);
                        panel.add(text);

                        JBPopupFactory.getInstance().createComponentPopupBuilder(panel,text).setRequestFocus(true).createPopup().showInFocusCenter();
                    }

                }

            }
        });
    }
}
