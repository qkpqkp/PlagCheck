# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QOpenGLTexture(__sip.simplewrapper):
    """
    QOpenGLTexture(QOpenGLTexture.Target)
    QOpenGLTexture(QImage, genMipMaps: QOpenGLTexture.MipMapGeneration = QOpenGLTexture.GenerateMipMaps)
    """
    def allocateStorage(self, QOpenGLTexture_PixelFormat=None, QOpenGLTexture_PixelType=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        allocateStorage(self)
        allocateStorage(self, QOpenGLTexture.PixelFormat, QOpenGLTexture.PixelType)
        """
        pass

    def bind(self, p_int=None, reset=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        bind(self)
        bind(self, int, reset: QOpenGLTexture.TextureUnitReset = QOpenGLTexture.DontResetTextureUnit)
        """
        pass

    def borderColor(self): # real signature unknown; restored from __doc__
        """ borderColor(self) -> QColor """
        return QColor

    def boundTextureId(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        boundTextureId(QOpenGLTexture.BindingTarget) -> int
        boundTextureId(int, QOpenGLTexture.BindingTarget) -> int
        """
        return 0

    def comparisonFunction(self): # real signature unknown; restored from __doc__
        """ comparisonFunction(self) -> QOpenGLTexture.ComparisonFunction """
        pass

    def comparisonMode(self): # real signature unknown; restored from __doc__
        """ comparisonMode(self) -> QOpenGLTexture.ComparisonMode """
        pass

    def create(self): # real signature unknown; restored from __doc__
        """ create(self) -> bool """
        return False

    def createTextureView(self, QOpenGLTexture_Target, QOpenGLTexture_TextureFormat, p_int, p_int_1, p_int_2, p_int_3): # real signature unknown; restored from __doc__
        """ createTextureView(self, QOpenGLTexture.Target, QOpenGLTexture.TextureFormat, int, int, int, int) -> QOpenGLTexture """
        return QOpenGLTexture

    def depth(self): # real signature unknown; restored from __doc__
        """ depth(self) -> int """
        return 0

    def depthStencilMode(self): # real signature unknown; restored from __doc__
        """ depthStencilMode(self) -> QOpenGLTexture.DepthStencilMode """
        pass

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def faces(self): # real signature unknown; restored from __doc__
        """ faces(self) -> int """
        return 0

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QOpenGLTexture.TextureFormat """
        pass

    def generateMipMaps(self, p_int=None, resetBaseLevel=True): # real signature unknown; restored from __doc__ with multiple overloads
        """
        generateMipMaps(self)
        generateMipMaps(self, int, resetBaseLevel: bool = True)
        """
        pass

    def hasFeature(self, QOpenGLTexture_Feature): # real signature unknown; restored from __doc__
        """ hasFeature(QOpenGLTexture.Feature) -> bool """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def isAutoMipMapGenerationEnabled(self): # real signature unknown; restored from __doc__
        """ isAutoMipMapGenerationEnabled(self) -> bool """
        return False

    def isBound(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isBound(self) -> bool
        isBound(self, int) -> bool
        """
        return False

    def isCreated(self): # real signature unknown; restored from __doc__
        """ isCreated(self) -> bool """
        return False

    def isFixedSamplePositions(self): # real signature unknown; restored from __doc__
        """ isFixedSamplePositions(self) -> bool """
        return False

    def isStorageAllocated(self): # real signature unknown; restored from __doc__
        """ isStorageAllocated(self) -> bool """
        return False

    def isTextureView(self): # real signature unknown; restored from __doc__
        """ isTextureView(self) -> bool """
        return False

    def layers(self): # real signature unknown; restored from __doc__
        """ layers(self) -> int """
        return 0

    def levelofDetailBias(self): # real signature unknown; restored from __doc__
        """ levelofDetailBias(self) -> float """
        return 0.0

    def levelOfDetailRange(self): # real signature unknown; restored from __doc__
        """ levelOfDetailRange(self) -> Tuple[float, float] """
        pass

    def magnificationFilter(self): # real signature unknown; restored from __doc__
        """ magnificationFilter(self) -> QOpenGLTexture.Filter """
        pass

    def maximumAnisotropy(self): # real signature unknown; restored from __doc__
        """ maximumAnisotropy(self) -> float """
        return 0.0

    def maximumLevelOfDetail(self): # real signature unknown; restored from __doc__
        """ maximumLevelOfDetail(self) -> float """
        return 0.0

    def maximumMipLevels(self): # real signature unknown; restored from __doc__
        """ maximumMipLevels(self) -> int """
        return 0

    def minificationFilter(self): # real signature unknown; restored from __doc__
        """ minificationFilter(self) -> QOpenGLTexture.Filter """
        pass

    def minimumLevelOfDetail(self): # real signature unknown; restored from __doc__
        """ minimumLevelOfDetail(self) -> float """
        return 0.0

    def minMagFilters(self): # real signature unknown; restored from __doc__
        """ minMagFilters(self) -> Tuple[QOpenGLTexture.Filter, QOpenGLTexture.Filter] """
        pass

    def mipBaseLevel(self): # real signature unknown; restored from __doc__
        """ mipBaseLevel(self) -> int """
        return 0

    def mipLevelRange(self): # real signature unknown; restored from __doc__
        """ mipLevelRange(self) -> Tuple[int, int] """
        pass

    def mipLevels(self): # real signature unknown; restored from __doc__
        """ mipLevels(self) -> int """
        return 0

    def mipMaxLevel(self): # real signature unknown; restored from __doc__
        """ mipMaxLevel(self) -> int """
        return 0

    def release(self, p_int=None, reset=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        release(self)
        release(self, int, reset: QOpenGLTexture.TextureUnitReset = QOpenGLTexture.DontResetTextureUnit)
        """
        pass

    def samples(self): # real signature unknown; restored from __doc__
        """ samples(self) -> int """
        return 0

    def setAutoMipMapGenerationEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setAutoMipMapGenerationEnabled(self, bool) """
        pass

    def setBorderColor(self, Union, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setBorderColor(self, Union[QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setComparisonFunction(self, QOpenGLTexture_ComparisonFunction): # real signature unknown; restored from __doc__
        """ setComparisonFunction(self, QOpenGLTexture.ComparisonFunction) """
        pass

    def setComparisonMode(self, QOpenGLTexture_ComparisonMode): # real signature unknown; restored from __doc__
        """ setComparisonMode(self, QOpenGLTexture.ComparisonMode) """
        pass

    def setCompressedData(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setCompressedData(self, int, int, QOpenGLTexture.CubeMapFace, int, sip.voidptr, options: QOpenGLPixelTransferOptions = None)
        setCompressedData(self, int, int, int, sip.voidptr, options: QOpenGLPixelTransferOptions = None)
        setCompressedData(self, int, int, sip.voidptr, options: QOpenGLPixelTransferOptions = None)
        setCompressedData(self, int, sip.voidptr, options: QOpenGLPixelTransferOptions = None)
        setCompressedData(self, int, int, int, QOpenGLTexture.CubeMapFace, int, sip.voidptr, options: QOpenGLPixelTransferOptions = None)
        """
        pass

    def setData(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setData(self, int, int, QOpenGLTexture.CubeMapFace, QOpenGLTexture.PixelFormat, QOpenGLTexture.PixelType, sip.voidptr, options: QOpenGLPixelTransferOptions = None)
        setData(self, int, int, QOpenGLTexture.PixelFormat, QOpenGLTexture.PixelType, sip.voidptr, options: QOpenGLPixelTransferOptions = None)
        setData(self, int, QOpenGLTexture.PixelFormat, QOpenGLTexture.PixelType, sip.voidptr, options: QOpenGLPixelTransferOptions = None)
        setData(self, QOpenGLTexture.PixelFormat, QOpenGLTexture.PixelType, sip.voidptr, options: QOpenGLPixelTransferOptions = None)
        setData(self, QImage, genMipMaps: QOpenGLTexture.MipMapGeneration = QOpenGLTexture.GenerateMipMaps)
        setData(self, int, int, int, QOpenGLTexture.CubeMapFace, QOpenGLTexture.PixelFormat, QOpenGLTexture.PixelType, sip.voidptr, options: QOpenGLPixelTransferOptions = None)
        """
        pass

    def setDepthStencilMode(self, QOpenGLTexture_DepthStencilMode): # real signature unknown; restored from __doc__
        """ setDepthStencilMode(self, QOpenGLTexture.DepthStencilMode) """
        pass

    def setFixedSamplePositions(self, bool): # real signature unknown; restored from __doc__
        """ setFixedSamplePositions(self, bool) """
        pass

    def setFormat(self, QOpenGLTexture_TextureFormat): # real signature unknown; restored from __doc__
        """ setFormat(self, QOpenGLTexture.TextureFormat) """
        pass

    def setLayers(self, p_int): # real signature unknown; restored from __doc__
        """ setLayers(self, int) """
        pass

    def setLevelofDetailBias(self, p_float): # real signature unknown; restored from __doc__
        """ setLevelofDetailBias(self, float) """
        pass

    def setLevelOfDetailRange(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ setLevelOfDetailRange(self, float, float) """
        pass

    def setMagnificationFilter(self, QOpenGLTexture_Filter): # real signature unknown; restored from __doc__
        """ setMagnificationFilter(self, QOpenGLTexture.Filter) """
        pass

    def setMaximumAnisotropy(self, p_float): # real signature unknown; restored from __doc__
        """ setMaximumAnisotropy(self, float) """
        pass

    def setMaximumLevelOfDetail(self, p_float): # real signature unknown; restored from __doc__
        """ setMaximumLevelOfDetail(self, float) """
        pass

    def setMinificationFilter(self, QOpenGLTexture_Filter): # real signature unknown; restored from __doc__
        """ setMinificationFilter(self, QOpenGLTexture.Filter) """
        pass

    def setMinimumLevelOfDetail(self, p_float): # real signature unknown; restored from __doc__
        """ setMinimumLevelOfDetail(self, float) """
        pass

    def setMinMagFilters(self, QOpenGLTexture_Filter, QOpenGLTexture_Filter_1): # real signature unknown; restored from __doc__
        """ setMinMagFilters(self, QOpenGLTexture.Filter, QOpenGLTexture.Filter) """
        pass

    def setMipBaseLevel(self, p_int): # real signature unknown; restored from __doc__
        """ setMipBaseLevel(self, int) """
        pass

    def setMipLevelRange(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setMipLevelRange(self, int, int) """
        pass

    def setMipLevels(self, p_int): # real signature unknown; restored from __doc__
        """ setMipLevels(self, int) """
        pass

    def setMipMaxLevel(self, p_int): # real signature unknown; restored from __doc__
        """ setMipMaxLevel(self, int) """
        pass

    def setSamples(self, p_int): # real signature unknown; restored from __doc__
        """ setSamples(self, int) """
        pass

    def setSize(self, p_int, height=1, depth=1): # real signature unknown; restored from __doc__
        """ setSize(self, int, height: int = 1, depth: int = 1) """
        pass

    def setSwizzleMask(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setSwizzleMask(self, QOpenGLTexture.SwizzleComponent, QOpenGLTexture.SwizzleValue)
        setSwizzleMask(self, QOpenGLTexture.SwizzleValue, QOpenGLTexture.SwizzleValue, QOpenGLTexture.SwizzleValue, QOpenGLTexture.SwizzleValue)
        """
        pass

    def setWrapMode(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setWrapMode(self, QOpenGLTexture.WrapMode)
        setWrapMode(self, QOpenGLTexture.CoordinateDirection, QOpenGLTexture.WrapMode)
        """
        pass

    def swizzleMask(self, QOpenGLTexture_SwizzleComponent): # real signature unknown; restored from __doc__
        """ swizzleMask(self, QOpenGLTexture.SwizzleComponent) -> QOpenGLTexture.SwizzleValue """
        pass

    def target(self): # real signature unknown; restored from __doc__
        """ target(self) -> QOpenGLTexture.Target """
        pass

    def textureId(self): # real signature unknown; restored from __doc__
        """ textureId(self) -> int """
        return 0

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

    def wrapMode(self, QOpenGLTexture_CoordinateDirection): # real signature unknown; restored from __doc__
        """ wrapMode(self, QOpenGLTexture.CoordinateDirection) -> QOpenGLTexture.WrapMode """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Alpha = 6406
    AlphaFormat = 6406
    AlphaValue = 6406
    AnisotropicFiltering = 1024
    BGR = 32992
    BGRA = 32993
    BGRA_Integer = 36251
    BGR_Integer = 36250
    BindingTarget1D = 32872
    BindingTarget1DArray = 35868
    BindingTarget2D = 32873
    BindingTarget2DArray = 35869
    BindingTarget2DMultisample = 37124
    BindingTarget2DMultisampleArray = 37125
    BindingTarget3D = 32874
    BindingTargetBuffer = 35884
    BindingTargetCubeMap = 34068
    BindingTargetCubeMapArray = 36874
    BindingTargetRectangle = 34038
    BlueValue = 6405
    ClampToBorder = 33069
    ClampToEdge = 33071
    CommpareNotEqual = 517
    CompareAlways = 519
    CompareEqual = 514
    CompareGreater = 516
    CompareGreaterEqual = 518
    CompareLess = 513
    CompareLessEqual = 515
    CompareNever = 512
    CompareNone = 0
    CompareRefToTexture = 34894
    CubeMapNegativeX = 34070
    CubeMapNegativeY = 34072
    CubeMapNegativeZ = 34074
    CubeMapPositiveX = 34069
    CubeMapPositiveY = 34071
    CubeMapPositiveZ = 34073
    D16 = 33189
    D24 = 33190
    D24S8 = 35056
    D32 = 33191
    D32F = 36012
    D32FS8X24 = 36013
    Depth = 6402
    DepthFormat = 6402
    DepthMode = 6402
    DepthStencil = 34041
    DirectionR = 32882
    DirectionS = 10242
    DirectionT = 10243
    DontGenerateMipMaps = 1
    DontResetTextureUnit = 1
    Float16 = 5131
    Float16OES = 36193
    Float32 = 5126
    Float32_D32_UInt32_S8_X24 = 36269
    GenerateMipMaps = 0
    GreenValue = 6404
    ImmutableMultisampleStorage = 2
    ImmutableStorage = 1
    Int16 = 5122
    Int32 = 5124
    Int8 = 5120
    Linear = 9729
    LinearMipMapLinear = 9987
    LinearMipMapNearest = 9985
    Luminance = 6409
    LuminanceAlpha = 6410
    LuminanceAlphaFormat = 6410
    LuminanceFormat = 6409
    MirroredRepeat = 33648
    Nearest = 9728
    NearestMipMapLinear = 9986
    NearestMipMapNearest = 9984
    NoFormat = 0
    NoPixelType = 0
    NoSourceFormat = 0
    NPOTTextureRepeat = 4096
    NPOTTextures = 2048
    OneValue = 1
    R11_EAC_SNorm = 37489
    R11_EAC_UNorm = 37488
    R16F = 33325
    R16I = 33331
    R16U = 33332
    R16_SNorm = 36760
    R16_UNorm = 33322
    R32F = 33326
    R32I = 33333
    R32U = 33334
    R5G6B5 = 36194
    R8I = 33329
    R8U = 33330
    R8_SNorm = 36756
    R8_UNorm = 33321
    Red = 6403
    RedValue = 6403
    Red_Integer = 36244
    Repeat = 10497
    ResetTextureUnit = 0
    RG = 33319
    RG11B10F = 35898
    RG11_EAC_SNorm = 37491
    RG11_EAC_UNorm = 37490
    RG16F = 33327
    RG16I = 33337
    RG16U = 33338
    RG16_SNorm = 36761
    RG16_UNorm = 33324
    RG32F = 33328
    RG32I = 33339
    RG32U = 33340
    RG3B2 = 10768
    RG8I = 33335
    RG8U = 33336
    RG8_SNorm = 36757
    RG8_UNorm = 33323
    RGB = 6407
    RGB10A2 = 36975
    RGB16F = 34843
    RGB16I = 36233
    RGB16U = 36215
    RGB16_SNorm = 36762
    RGB16_UNorm = 32852
    RGB32F = 34837
    RGB32I = 36227
    RGB32U = 36209
    RGB5A1 = 32855
    RGB8I = 36239
    RGB8U = 36221
    RGB8_ETC1 = 36196
    RGB8_ETC2 = 37492
    RGB8_PunchThrough_Alpha1_ETC2 = 37494
    RGB8_SNorm = 36758
    RGB8_UNorm = 32849
    RGB9E5 = 35901
    RGBA = 6408
    RGBA16F = 34842
    RGBA16I = 36232
    RGBA16U = 36214
    RGBA16_SNorm = 36763
    RGBA16_UNorm = 32859
    RGBA32F = 34836
    RGBA32I = 36226
    RGBA32U = 36208
    RGBA4 = 32854
    RGBA8I = 36238
    RGBA8U = 36220
    RGBA8_ETC2_EAC = 37496
    RGBA8_SNorm = 36759
    RGBA8_UNorm = 32856
    RGBAFormat = 6408
    RGBA_ASTC_10x10 = 37819
    RGBA_ASTC_10x5 = 37816
    RGBA_ASTC_10x6 = 37817
    RGBA_ASTC_10x8 = 37818
    RGBA_ASTC_12x10 = 37820
    RGBA_ASTC_12x12 = 37821
    RGBA_ASTC_4x4 = 37808
    RGBA_ASTC_5x4 = 37809
    RGBA_ASTC_5x5 = 37810
    RGBA_ASTC_6x5 = 37811
    RGBA_ASTC_6x6 = 37812
    RGBA_ASTC_8x5 = 37813
    RGBA_ASTC_8x6 = 37814
    RGBA_ASTC_8x8 = 37815
    RGBA_DXT1 = 33777
    RGBA_DXT3 = 33778
    RGBA_DXT5 = 33779
    RGBA_Integer = 36249
    RGBFormat = 6407
    RGB_BP_SIGNED_FLOAT = 36494
    RGB_BP_UNorm = 36492
    RGB_BP_UNSIGNED_FLOAT = 36495
    RGB_DXT1 = 33776
    RGB_Integer = 36248
    RG_ATI2N_SNorm = 36286
    RG_ATI2N_UNorm = 36285
    RG_Integer = 33320
    R_ATI1N_SNorm = 36284
    R_ATI1N_UNorm = 36283
    S8 = 36168
    SRGB8 = 35905
    SRGB8_Alpha8 = 35907
    SRGB8_Alpha8_ASTC_10x10 = 37851
    SRGB8_Alpha8_ASTC_10x5 = 37848
    SRGB8_Alpha8_ASTC_10x6 = 37849
    SRGB8_Alpha8_ASTC_10x8 = 37850
    SRGB8_Alpha8_ASTC_12x10 = 37852
    SRGB8_Alpha8_ASTC_12x12 = 37853
    SRGB8_Alpha8_ASTC_4x4 = 37840
    SRGB8_Alpha8_ASTC_5x4 = 37841
    SRGB8_Alpha8_ASTC_5x5 = 37842
    SRGB8_Alpha8_ASTC_6x5 = 37843
    SRGB8_Alpha8_ASTC_6x6 = 37844
    SRGB8_Alpha8_ASTC_8x5 = 37845
    SRGB8_Alpha8_ASTC_8x6 = 37846
    SRGB8_Alpha8_ASTC_8x8 = 37847
    SRGB8_Alpha8_ETC2_EAC = 37497
    SRGB8_ETC2 = 37493
    SRGB8_PunchThrough_Alpha1_ETC2 = 37495
    SRGB_Alpha_DXT1 = 35917
    SRGB_Alpha_DXT3 = 35918
    SRGB_Alpha_DXT5 = 35919
    SRGB_BP_UNorm = 36493
    SRGB_DXT1 = 35916
    Stencil = 6401
    StencilMode = 6401
    StencilTexturing = 512
    Swizzle = 256
    SwizzleAlpha = 36421
    SwizzleBlue = 36420
    SwizzleGreen = 36419
    SwizzleRed = 36418
    Target1D = 3552
    Target1DArray = 35864
    Target2D = 3553
    Target2DArray = 35866
    Target2DMultisample = 37120
    Target2DMultisampleArray = 37122
    Target3D = 32879
    TargetBuffer = 35882
    TargetCubeMap = 34067
    TargetCubeMapArray = 36873
    TargetRectangle = 34037
    Texture1D = 8192
    Texture3D = 16
    TextureArrays = 8
    TextureBuffer = 64
    TextureComparisonOperators = 16384
    TextureCubeMapArrays = 128
    TextureMipMapLevel = 32768
    TextureMultisample = 32
    TextureRectangle = 4
    UInt16 = 5123
    UInt16_R5G6B5 = 33635
    UInt16_R5G6B5_Rev = 33636
    UInt16_RGB5A1 = 32820
    UInt16_RGB5A1_Rev = 33638
    UInt16_RGBA4 = 32819
    UInt16_RGBA4_Rev = 33637
    UInt32 = 5125
    UInt32_D24S8 = 34042
    UInt32_RG11B10F = 35899
    UInt32_RGB10A2 = 32822
    UInt32_RGB10A2_Rev = 33640
    UInt32_RGB9_E5 = 35902
    UInt32_RGBA8 = 32821
    UInt32_RGBA8_Rev = 33639
    UInt8 = 5121
    UInt8_RG3B2 = 32818
    UInt8_RG3B2_Rev = 33634
    ZeroValue = 0


