package com.plagcheck;

import com.intellij.openapi.actionSystem.AnAction;
import com.intellij.openapi.actionSystem.AnActionEvent;
import com.intellij.openapi.editor.Document;
import com.intellij.openapi.editor.Editor;
import com.intellij.openapi.fileEditor.FileDocumentManager;
import com.intellij.openapi.fileEditor.FileEditorManager;
import com.intellij.openapi.vfs.VirtualFile;
import com.intellij.ui.BrowserHyperlinkListener;
import org.jetbrains.annotations.NotNull;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import javax.swing.*;
import javax.swing.event.HyperlinkListener;
import java.io.*;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.util.List;
import java.util.concurrent.TimeUnit;

public class PlagiarismDetection extends AnAction {
    /**
     * Searching for similar codes using Google with part of the code
     * Jsoup is used to do the request
     * @param src
     * @return A map that maps url to code
     */
    private Map<String,String> retrieveFromGit(String src){
        Map<String, String> CodeMap = new HashMap<>();
        String key = "AIzaSyB-UHIT2lz1Hw-XyeFAQ7dJW67mNWCDnKg";
        String cx = "007835117730733246990:1ek1-aykdo4";
        src = URLEncoder.encode(src, StandardCharsets.UTF_8);
        if(src.length()>800){ //url cannot be too long, limit the length of code
            src=src.substring(0,800);
        }
        String search_url = "https://www.googleapis.com/customsearch/v1?key=" + key + "&cx=" + cx + "&q=" + src;
        String json;
        try {
            json = Jsoup.connect(search_url).ignoreContentType(true).execute().body();
        }catch (IOException e){
            return null;
        }
        JSONObject obj = new JSONObject(json);

        JSONArray items; //Bad implementation, need to refactor
        try{
            items = obj.getJSONArray("items");
        }catch (JSONException e){
            return CodeMap;
        }
        int count = 0;
        for (int i = 0; i < items.length(); i++) {
            if (count > 10) { //Limit the number of links, otherwise it will take too long
                break;
            }
            JSONObject item = items.getJSONObject(i);
            String link = item.getString("link");
            if (CodeMap.keySet().contains(link)) { //If already exist
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
                //Get the link to raw Python code
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

    /**
     * Abandoned temporarily. Search with each line of code. Too expensive.
     * @param src
     * @return A map that maps url to code
     */
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
                    /* Stackoverflow doesn't work because attributes are missing
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

    /**
     * Run the code comparison algorithm written in Python
     * @param src_code
     * @param susp_code
     * @return A result string generated by the code comparison algorithm
     * @throws FileNotFoundException
     */
    private String checkPlag(String src_code,String susp_code) throws FileNotFoundException {
        Runtime r = Runtime.getRuntime();
        String [] cmd = new String[2]; //Setup a command to run a Python script
        cmd[0] = "python";
        //Should change to relative path
        cmd[1] = "C:\\Users\\Doly\\PlagCheck\\src\\main\\resources\\PlagCheck1.1.py";
        PrintWriter out1 = new PrintWriter("C:\\Users\\Doly\\PlagCheck\\src\\main\\resources\\code1.py");
        //Put codes temporarily into files because some characters in code cannot be put in arguments of a command
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
            if(!p.waitFor(1, TimeUnit.SECONDS)) { //If it takes too long, withdraw
                p.destroy();
            }
            int count = 0;
            while((s=in.readLine()) != null){ //Read from Python "print()"
                resultString=s;
            }
            /* For debug purposes, read error messages
            BufferedReader err = new BufferedReader(new InputStreamReader(p.getErrorStream()));
            while((s=err.readLine()) != null){
                System.out.println(s);
            }*/
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }

        return resultString;
    }

    /**
     * Parse the result string
     * @param resultString
     * @return A mapping between lines that are suspected to be plagiarized and
     * lines that are similar to the suspected line
     */
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

    /**
     * Run the plugin
     * Refactoring required
     * @param e
     */
    @Override
    public void actionPerformed(@NotNull AnActionEvent e) {
        List<String> sources = new ArrayList<>(); //List of links
        List<Double> similarities = new ArrayList<>(); //List of similarities
        List<Integer> lengths = new ArrayList<>(); //List of length of files
        Editor editor = FileEditorManager.getInstance(e.getProject()).getSelectedTextEditor();
        Document currentdoc = editor.getDocument();
        String susp = currentdoc.getText(); //Codes from the PyCharm editor
        Thread thread = new Thread(){//Use a thread to avoid PyCharm from freezing
            public void run(){
                Map<String, String> CodeMap; //Maps links to code
                CodeMap = retrieveFromGit(susp);
                for(String s:CodeMap.keySet()) {
                    Map<Integer, List<Integer>> result = new HashMap<>(); //Result
                    try {
                        String resultString = checkPlag(CodeMap.get(s),susp);
                        result = parseResult(resultString);
                        if(result==null){ //If result cannnot be parsed (empty string?)
                            continue;
                        }
                    } catch (FileNotFoundException fileNotFoundException) {
                        fileNotFoundException.printStackTrace();
                    }
                    String[] lines = susp.split("\n");
                    int line_count = 0;
                    for(String line:lines){ //Don't count comments and empty lines
                        if(line.strip().startsWith("#")){
                            continue;
                        }
                        if(line.equals("")){
                            continue;
                        }
                        line_count++;
                    }
                    double similarity = (double)result.keySet().size() / line_count;
                    if (similarity > 0.5) { //Threshold of warning
                        sources.add(s);
                        similarities.add(similarity);
                        lengths.add(CodeMap.get(s).split("\n").length);
                    }
                }
                if(sources.size()>0) { //If there are codes from github similar to codes in the editor
                    String text = "";
                    VirtualFile currentFile = FileDocumentManager.getInstance().getFile(currentdoc);
                    String fileName = currentFile.getPath();
                    int count=0;
                    for(String s:sources){ //Construct a message from the existing data
                        count++;
                        text=text.concat(count+". Length: "+lengths.get(count-1)+", Similarity: "+similarities.get(count-1)+", Link: ");
                        text=text.concat("<a href=\""+s+"\">"+s+"</a><br>");
                    }
                    /*
                    Setup a panel to show user the result
                    */
                    JDialog dialog = new JDialog();
                    dialog.setTitle(fileName + " is suspected for plagiarism");
                    dialog.setModal(true);
                    dialog.setSize(800,600);
                    JEditorPane editorPane = new JEditorPane();
                    editorPane.setSize(800,600);
                    dialog.setContentPane(editorPane);
                    editorPane.setEditorKit(JEditorPane.createEditorKitForContentType("text/html"));
                    editorPane.setEditable(false);
                    HyperlinkListener hyperlinkListener = new BrowserHyperlinkListener();
                    editorPane.addHyperlinkListener(hyperlinkListener);
                    editorPane.setText(text);
                    dialog.setVisible(true);

                }else{ //No plagiarism detected
                    JFrame f = new JFrame();
                    JOptionPane.showMessageDialog(f,"No plagiarism detected");
                }
            }
        };
        thread.start();
    }
}
