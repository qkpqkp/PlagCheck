# encoding: utf-8
# module cv2.cv2
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
""" Python wrapper for OpenCV. """

# imports
import cv2.cv2 as  # C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
import cv2.Error as Error # <module 'cv2.Error'>
import cv2.aruco as aruco # <module 'cv2.aruco'>
import cv2.bgsegm as bgsegm # <module 'cv2.bgsegm'>
import cv2.bioinspired as bioinspired # <module 'cv2.bioinspired'>
import cv2.cuda as cuda # <module 'cv2.cuda'>
import cv2.datasets as datasets # <module 'cv2.datasets'>
import cv2.detail as detail # <module 'cv2.detail'>
import cv2.dnn as dnn # <module 'cv2.dnn'>
import cv2.face as face # <module 'cv2.face'>
import cv2.fisheye as fisheye # <module 'cv2.fisheye'>
import cv2.flann as flann # <module 'cv2.flann'>
import cv2.ft as ft # <module 'cv2.ft'>
import cv2.hfs as hfs # <module 'cv2.hfs'>
import cv2.img_hash as img_hash # <module 'cv2.img_hash'>
import cv2.instr as instr # <module 'cv2.instr'>
import cv2.ipp as ipp # <module 'cv2.ipp'>
import cv2.kinfu as kinfu # <module 'cv2.kinfu'>
import cv2.line_descriptor as line_descriptor # <module 'cv2.line_descriptor'>
import cv2.linemod as linemod # <module 'cv2.linemod'>
import cv2.ml as ml # <module 'cv2.ml'>
import cv2.motempl as motempl # <module 'cv2.motempl'>
import cv2.multicalib as multicalib # <module 'cv2.multicalib'>
import cv2.ocl as ocl # <module 'cv2.ocl'>
import cv2.ogl as ogl # <module 'cv2.ogl'>
import cv2.omnidir as omnidir # <module 'cv2.omnidir'>
import cv2.optflow as optflow # <module 'cv2.optflow'>
import cv2.plot as plot # <module 'cv2.plot'>
import cv2.ppf_match_3d as ppf_match_3d # <module 'cv2.ppf_match_3d'>
import cv2.quality as quality # <module 'cv2.quality'>
import cv2.reg as reg # <module 'cv2.reg'>
import cv2.rgbd as rgbd # <module 'cv2.rgbd'>
import cv2.saliency as saliency # <module 'cv2.saliency'>
import cv2.samples as samples # <module 'cv2.samples'>
import cv2.structured_light as structured_light # <module 'cv2.structured_light'>
import cv2.text as text # <module 'cv2.text'>
import cv2.utils as utils # <module 'cv2.utils'>
import cv2.videoio_registry as videoio_registry # <module 'cv2.videoio_registry'>
import cv2.videostab as videostab # <module 'cv2.videostab'>
import cv2.xfeatures2d as xfeatures2d # <module 'cv2.xfeatures2d'>
import cv2.ximgproc as ximgproc # <module 'cv2.ximgproc'>
import cv2.xphoto as xphoto # <module 'cv2.xphoto'>
import cv2 as __cv2


from .object import object

class Subdiv2D(object):
    # no doc
    def edgeDst(self, edge): # real signature unknown; restored from __doc__
        """
        edgeDst(edge) -> retval, dstpt
        .   @brief Returns the edge destination.
        .   
        .       @param edge Subdivision edge ID.
        .       @param dstpt Output vertex location.
        .   
        .       @returns vertex ID.
        """
        pass

    def edgeOrg(self, edge): # real signature unknown; restored from __doc__
        """
        edgeOrg(edge) -> retval, orgpt
        .   @brief Returns the edge origin.
        .   
        .       @param edge Subdivision edge ID.
        .       @param orgpt Output vertex location.
        .   
        .       @returns vertex ID.
        """
        pass

    def findNearest(self, pt): # real signature unknown; restored from __doc__
        """
        findNearest(pt) -> retval, nearestPt
        .   @brief Finds the subdivision vertex closest to the given point.
        .   
        .       @param pt Input point.
        .       @param nearestPt Output subdivision vertex point.
        .   
        .       The function is another function that locates the input point within the subdivision. It finds the
        .       subdivision vertex that is the closest to the input point. It is not necessarily one of vertices
        .       of the facet containing the input point, though the facet (located using locate() ) is used as a
        .       starting point.
        .   
        .       @returns vertex ID.
        """
        pass

    def getEdge(self, edge, nextEdgeType): # real signature unknown; restored from __doc__
        """
        getEdge(edge, nextEdgeType) -> retval
        .   @brief Returns one of the edges related to the given edge.
        .   
        .       @param edge Subdivision edge ID.
        .       @param nextEdgeType Parameter specifying which of the related edges to return.
        .       The following values are possible:
        .       -   NEXT_AROUND_ORG next around the edge origin ( eOnext on the picture below if e is the input edge)
        .       -   NEXT_AROUND_DST next around the edge vertex ( eDnext )
        .       -   PREV_AROUND_ORG previous around the edge origin (reversed eRnext )
        .       -   PREV_AROUND_DST previous around the edge destination (reversed eLnext )
        .       -   NEXT_AROUND_LEFT next around the left facet ( eLnext )
        .       -   NEXT_AROUND_RIGHT next around the right facet ( eRnext )
        .       -   PREV_AROUND_LEFT previous around the left facet (reversed eOnext )
        .       -   PREV_AROUND_RIGHT previous around the right facet (reversed eDnext )
        .   
        .       ![sample output](pics/quadedge.png)
        .   
        .       @returns edge ID related to the input edge.
        """
        pass

    def getEdgeList(self): # real signature unknown; restored from __doc__
        """
        getEdgeList() -> edgeList
        .   @brief Returns a list of all edges.
        .   
        .       @param edgeList Output vector.
        .   
        .       The function gives each edge as a 4 numbers vector, where each two are one of the edge
        .       vertices. i.e. org_x = v[0], org_y = v[1], dst_x = v[2], dst_y = v[3].
        """
        pass

    def getLeadingEdgeList(self): # real signature unknown; restored from __doc__
        """
        getLeadingEdgeList() -> leadingEdgeList
        .   @brief Returns a list of the leading edge ID connected to each triangle.
        .   
        .       @param leadingEdgeList Output vector.
        .   
        .       The function gives one edge ID for each triangle.
        """
        pass

    def getTriangleList(self): # real signature unknown; restored from __doc__
        """
        getTriangleList() -> triangleList
        .   @brief Returns a list of all triangles.
        .   
        .       @param triangleList Output vector.
        .   
        .       The function gives each triangle as a 6 numbers vector, where each two are one of the triangle
        .       vertices. i.e. p1_x = v[0], p1_y = v[1], p2_x = v[2], p2_y = v[3], p3_x = v[4], p3_y = v[5].
        """
        pass

    def getVertex(self, vertex): # real signature unknown; restored from __doc__
        """
        getVertex(vertex) -> retval, firstEdge
        .   @brief Returns vertex location from vertex ID.
        .   
        .       @param vertex vertex ID.
        .       @param firstEdge Optional. The first edge ID which is connected to the vertex.
        .       @returns vertex (x,y)
        """
        pass

    def getVoronoiFacetList(self, idx): # real signature unknown; restored from __doc__
        """
        getVoronoiFacetList(idx) -> facetList, facetCenters
        .   @brief Returns a list of all Voroni facets.
        .   
        .       @param idx Vector of vertices IDs to consider. For all vertices you can pass empty vector.
        .       @param facetList Output vector of the Voroni facets.
        .       @param facetCenters Output vector of the Voroni facets center points.
        """
        pass

    def initDelaunay(self, rect): # real signature unknown; restored from __doc__
        """
        initDelaunay(rect) -> None
        .   @brief Creates a new empty Delaunay subdivision
        .   
        .       @param rect Rectangle that includes all of the 2D points that are to be added to the subdivision.
        """
        pass

    def insert(self, pt): # real signature unknown; restored from __doc__
        """
        insert(pt) -> retval
        .   @brief Insert a single point into a Delaunay triangulation.
        .   
        .       @param pt Point to insert.
        .   
        .       The function inserts a single point into a subdivision and modifies the subdivision topology
        .       appropriately. If a point with the same coordinates exists already, no new point is added.
        .       @returns the ID of the point.
        .   
        .       @note If the point is outside of the triangulation specified rect a runtime error is raised.
        
        
        
        insert(ptvec) -> None
        .   @brief Insert multiple points into a Delaunay triangulation.
        .   
        .       @param ptvec Points to insert.
        .   
        .       The function inserts a vector of points into a subdivision and modifies the subdivision topology
        .       appropriately.
        """
        pass

    def locate(self, pt): # real signature unknown; restored from __doc__
        """
        locate(pt) -> retval, edge, vertex
        .   @brief Returns the location of a point within a Delaunay triangulation.
        .   
        .       @param pt Point to locate.
        .       @param edge Output edge that the point belongs to or is located to the right of it.
        .       @param vertex Optional output vertex the input point coincides with.
        .   
        .       The function locates the input point within the subdivision and gives one of the triangle edges
        .       or vertices.
        .   
        .       @returns an integer which specify one of the following five cases for point location:
        .       -  The point falls into some facet. The function returns #PTLOC_INSIDE and edge will contain one of
        .          edges of the facet.
        .       -  The point falls onto the edge. The function returns #PTLOC_ON_EDGE and edge will contain this edge.
        .       -  The point coincides with one of the subdivision vertices. The function returns #PTLOC_VERTEX and
        .          vertex will contain a pointer to the vertex.
        .       -  The point is outside the subdivision reference rectangle. The function returns #PTLOC_OUTSIDE_RECT
        .          and no pointers are filled.
        .       -  One of input arguments is invalid. A runtime error is raised or, if silent or "parent" error
        .          processing mode is selected, #PTLOC_ERROR is returned.
        """
        pass

    def nextEdge(self, edge): # real signature unknown; restored from __doc__
        """
        nextEdge(edge) -> retval
        .   @brief Returns next edge around the edge origin.
        .   
        .       @param edge Subdivision edge ID.
        .   
        .       @returns an integer which is next edge ID around the edge origin: eOnext on the
        .       picture above if e is the input edge).
        """
        pass

    def rotateEdge(self, edge, rotate): # real signature unknown; restored from __doc__
        """
        rotateEdge(edge, rotate) -> retval
        .   @brief Returns another edge of the same quad-edge.
        .   
        .       @param edge Subdivision edge ID.
        .       @param rotate Parameter specifying which of the edges of the same quad-edge as the input
        .       one to return. The following values are possible:
        .       -   0 - the input edge ( e on the picture below if e is the input edge)
        .       -   1 - the rotated edge ( eRot )
        .       -   2 - the reversed edge (reversed e (in green))
        .       -   3 - the reversed rotated edge (reversed eRot (in green))
        .   
        .       @returns one of the edges ID of the same quad-edge as the input edge.
        """
        pass

    def symEdge(self, edge): # real signature unknown; restored from __doc__
        """
        symEdge(edge) -> retval
        .
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


