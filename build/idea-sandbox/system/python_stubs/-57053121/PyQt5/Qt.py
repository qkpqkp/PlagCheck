# encoding: utf-8
# module PyQt5.Qt
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\Qt.pyd
# by generator 1.147
# no doc

# imports
from PyQt5.QtBluetooth import (QBluetooth, QBluetoothAddress, 
    QBluetoothDeviceDiscoveryAgent, QBluetoothDeviceInfo, QBluetoothHostInfo, 
    QBluetoothLocalDevice, QBluetoothServer, QBluetoothServiceDiscoveryAgent, 
    QBluetoothServiceInfo, QBluetoothSocket, QBluetoothTransferManager, 
    QBluetoothTransferReply, QBluetoothTransferRequest, QBluetoothUuid, 
    QLowEnergyAdvertisingData, QLowEnergyAdvertisingParameters, 
    QLowEnergyCharacteristic, QLowEnergyCharacteristicData, 
    QLowEnergyConnectionParameters, QLowEnergyController, 
    QLowEnergyDescriptor, QLowEnergyDescriptorData, QLowEnergyService, 
    QLowEnergyServiceData)

from PyQt5.QtCore import (QAbstractAnimation, QAbstractEventDispatcher, 
    QAbstractItemModel, QAbstractListModel, QAbstractNativeEventFilter, 
    QAbstractProxyModel, QAbstractState, QAbstractTableModel, 
    QAbstractTransition, QAnimationGroup, QBasicTimer, QBitArray, QBuffer, 
    QByteArray, QByteArrayMatcher, QCborError, QCborKnownTags, 
    QCborSimpleType, QCborStreamReader, QCborStreamWriter, QChildEvent, 
    QCollator, QCollatorSortKey, QCommandLineOption, QCommandLineParser, 
    QCoreApplication, QCryptographicHash, QDataStream, QDate, QDateTime, 
    QDeadlineTimer, QDir, QDirIterator, QDynamicPropertyChangeEvent, 
    QEasingCurve, QElapsedTimer, QEvent, QEventLoop, QEventLoopLocker, 
    QEventTransition, QFile, QFileDevice, QFileInfo, QFileSelector, 
    QFileSystemWatcher, QFinalState, QGenericArgument, QGenericReturnArgument, 
    QHistoryState, QIODevice, QIdentityProxyModel, QItemSelection, 
    QItemSelectionModel, QItemSelectionRange, QJsonDocument, QJsonParseError, 
    QJsonValue, QLibrary, QLibraryInfo, QLine, QLineF, QLocale, QLockFile, 
    QLoggingCategory, QMargins, QMarginsF, QMessageAuthenticationCode, 
    QMessageLogContext, QMessageLogger, QMetaClassInfo, QMetaEnum, 
    QMetaMethod, QMetaObject, QMetaProperty, QMetaType, QMimeData, 
    QMimeDatabase, QMimeType, QModelIndex, QMutex, QMutexLocker, QObject, 
    QObjectCleanupHandler, QOperatingSystemVersion, QParallelAnimationGroup, 
    QPauseAnimation, QPersistentModelIndex, QPluginLoader, QPoint, QPointF, 
    QProcess, QProcessEnvironment, QPropertyAnimation, QRandomGenerator, 
    QReadLocker, QReadWriteLock, QRect, QRectF, QRegExp, QRegularExpression, 
    QRegularExpressionMatch, QRegularExpressionMatchIterator, QResource, 
    QRunnable, QSaveFile, QSemaphore, QSemaphoreReleaser, 
    QSequentialAnimationGroup, QSettings, QSharedMemory, QSignalBlocker, 
    QSignalMapper, QSignalTransition, QSize, QSizeF, QSocketNotifier, 
    QSortFilterProxyModel, QStandardPaths, QState, QStateMachine, 
    QStorageInfo, QStringListModel, QSysInfo, QSystemSemaphore, 
    QT_TRANSLATE_NOOP, QT_TR_NOOP, QT_TR_NOOP_UTF8, QTemporaryDir, 
    QTemporaryFile, QTextBoundaryFinder, QTextCodec, QTextDecoder, 
    QTextEncoder, QTextStream, QTextStreamManipulator, QThread, QThreadPool, 
    QTime, QTimeLine, QTimeZone, QTimer, QTimerEvent, QTranslator, QUrl, 
    QUrlQuery, QUuid, QVariant, QVariantAnimation, QVersionNumber, 
    QWaitCondition, QWinEventNotifier, QWriteLocker, QXmlStreamAttribute, 
    QXmlStreamAttributes, QXmlStreamEntityDeclaration, 
    QXmlStreamEntityResolver, QXmlStreamNamespaceDeclaration, 
    QXmlStreamNotationDeclaration, QXmlStreamReader, QXmlStreamWriter, Q_ARG, 
    Q_CLASSINFO, Q_ENUM, Q_ENUMS, Q_FLAG, Q_FLAGS, Q_RETURN_ARG, Qt, 
    QtCriticalMsg, QtDebugMsg, QtFatalMsg, QtInfoMsg, QtMsgType, QtSystemMsg, 
    QtWarningMsg, bin_, bom, center, dec, endl, fixed, flush, forcepoint, 
    forcesign, hex_, left, lowercasebase, lowercasedigits, noforcepoint, 
    noforcesign, noshowbase, oct_, pyqtBoundSignal, pyqtPickleProtocol, 
    pyqtProperty, pyqtRemoveInputHook, pyqtRestoreInputHook, 
    pyqtSetPickleProtocol, pyqtSignal, pyqtSlot, qAbs, qAddPostRoutine, 
    qAddPreRoutine, qChecksum, qCompress, qCritical, qDebug, 
    qEnvironmentVariable, qErrnoWarning, qFatal, qFloatDistance, 
    qFormatLogMessage, qFuzzyCompare, qInf, qInfo, qInstallMessageHandler, 
    qIsFinite, qIsInf, qIsNaN, qIsNull, qQNaN, qRegisterResourceData, 
    qRemovePostRoutine, qRound, qRound64, qSNaN, qSetFieldWidth, 
    qSetMessagePattern, qSetPadChar, qSetRealNumberPrecision, qSharedBuild, 
    qUncompress, qUnregisterResourceData, qVersion, qWarning, qrand, qsrand, 
    reset, right, scientific, showbase, uppercasebase, uppercasedigits, ws)

from PyQt5.QtDBus import (QDBus, QDBusAbstractAdaptor, QDBusAbstractInterface, 
    QDBusArgument, QDBusConnection, QDBusConnectionInterface, QDBusError, 
    QDBusInterface, QDBusMessage, QDBusObjectPath, QDBusPendingCall, 
    QDBusPendingCallWatcher, QDBusPendingReply, QDBusReply, 
    QDBusServiceWatcher, QDBusSignature, QDBusUnixFileDescriptor, 
    QDBusVariant)

from PyQt5.QtDesigner import (QAbstractExtensionFactory, 
    QAbstractExtensionManager, QAbstractFormBuilder, 
    QDesignerActionEditorInterface, QDesignerContainerExtension, 
    QDesignerCustomWidgetCollectionInterface, QDesignerCustomWidgetInterface, 
    QDesignerFormEditorInterface, QDesignerFormWindowCursorInterface, 
    QDesignerFormWindowInterface, QDesignerFormWindowManagerInterface, 
    QDesignerMemberSheetExtension, QDesignerObjectInspectorInterface, 
    QDesignerPropertyEditorInterface, QDesignerPropertySheetExtension, 
    QDesignerTaskMenuExtension, QDesignerWidgetBoxInterface, 
    QExtensionFactory, QExtensionManager, QFormBuilder, 
    QPyDesignerContainerExtension, QPyDesignerCustomWidgetCollectionPlugin, 
    QPyDesignerCustomWidgetPlugin, QPyDesignerMemberSheetExtension, 
    QPyDesignerPropertySheetExtension, QPyDesignerTaskMenuExtension)

from PyQt5.QtGui import (QAbstractOpenGLFunctions, 
    QAbstractTextDocumentLayout, QActionEvent, QBackingStore, QBitmap, QBrush, 
    QClipboard, QCloseEvent, QColor, QConicalGradient, QContextMenuEvent, 
    QCursor, QDesktopServices, QDoubleValidator, QDrag, QDragEnterEvent, 
    QDragLeaveEvent, QDragMoveEvent, QDropEvent, QEnterEvent, QExposeEvent, 
    QFileOpenEvent, QFocusEvent, QFont, QFontDatabase, QFontInfo, 
    QFontMetrics, QFontMetricsF, QGlyphRun, QGradient, QGuiApplication, 
    QHelpEvent, QHideEvent, QHoverEvent, QIcon, QIconDragEvent, QIconEngine, 
    QImage, QImageIOHandler, QImageReader, QImageWriter, QInputEvent, 
    QInputMethod, QInputMethodEvent, QInputMethodQueryEvent, QIntValidator, 
    QKeyEvent, QKeySequence, QLinearGradient, QMatrix2x2, QMatrix2x3, 
    QMatrix2x4, QMatrix3x2, QMatrix3x3, QMatrix3x4, QMatrix4x2, QMatrix4x3, 
    QMatrix4x4, QMouseEvent, QMoveEvent, QMovie, QNativeGestureEvent, 
    QOffscreenSurface, QOpenGLBuffer, QOpenGLContext, QOpenGLContextGroup, 
    QOpenGLDebugLogger, QOpenGLDebugMessage, QOpenGLFramebufferObject, 
    QOpenGLFramebufferObjectFormat, QOpenGLPaintDevice, 
    QOpenGLPixelTransferOptions, QOpenGLShader, QOpenGLShaderProgram, 
    QOpenGLTexture, QOpenGLTextureBlitter, QOpenGLTimeMonitor, 
    QOpenGLTimerQuery, QOpenGLVersionProfile, QOpenGLVertexArrayObject, 
    QOpenGLWindow, QPageLayout, QPageSize, QPagedPaintDevice, QPaintDevice, 
    QPaintDeviceWindow, QPaintEngine, QPaintEngineState, QPaintEvent, 
    QPainter, QPainterPath, QPainterPathStroker, QPalette, QPdfWriter, QPen, 
    QPicture, QPictureIO, QPixelFormat, QPixmap, QPixmapCache, 
    QPlatformSurfaceEvent, QPointingDeviceUniqueId, QPolygon, QPolygonF, 
    QQuaternion, QRadialGradient, QRasterWindow, QRawFont, QRegExpValidator, 
    QRegion, QRegularExpressionValidator, QResizeEvent, QRgba64, QScreen, 
    QScrollEvent, QScrollPrepareEvent, QSessionManager, QShortcutEvent, 
    QShowEvent, QStandardItem, QStandardItemModel, QStaticText, 
    QStatusTipEvent, QStyleHints, QSurface, QSurfaceFormat, 
    QSyntaxHighlighter, QTabletEvent, QTextBlock, QTextBlockFormat, 
    QTextBlockGroup, QTextBlockUserData, QTextCharFormat, QTextCursor, 
    QTextDocument, QTextDocumentFragment, QTextDocumentWriter, QTextFormat, 
    QTextFragment, QTextFrame, QTextFrameFormat, QTextImageFormat, 
    QTextInlineObject, QTextItem, QTextLayout, QTextLength, QTextLine, 
    QTextList, QTextListFormat, QTextObject, QTextObjectInterface, 
    QTextOption, QTextTable, QTextTableCell, QTextTableCellFormat, 
    QTextTableFormat, QTouchDevice, QTouchEvent, QTransform, QValidator, 
    QVector2D, QVector3D, QVector4D, QWhatsThisClickedEvent, QWheelEvent, 
    QWindow, QWindowStateChangeEvent, qAlpha, qBlue, qGray, qGreen, qIsGray, 
    qPixelFormatAlpha, qPixelFormatCmyk, qPixelFormatGrayscale, 
    qPixelFormatHsl, qPixelFormatHsv, qPixelFormatRgba, qPixelFormatYuv, 
    qPremultiply, qRed, qRgb, qRgba, qRgba64, qUnpremultiply, 
    qt_set_sequence_auto_mnemonic)

from PyQt5.QtHelp import (QHelpContentItem, QHelpContentModel, 
    QHelpContentWidget, QHelpEngine, QHelpEngineCore, QHelpIndexModel, 
    QHelpIndexWidget, QHelpSearchEngine, QHelpSearchQuery, 
    QHelpSearchQueryWidget, QHelpSearchResult, QHelpSearchResultWidget)

from PyQt5.QtLocation import (QGeoCodeReply, QGeoCodingManager, 
    QGeoCodingManagerEngine, QGeoManeuver, QGeoRoute, QGeoRouteLeg, 
    QGeoRouteReply, QGeoRouteRequest, QGeoRouteSegment, QGeoRoutingManager, 
    QGeoRoutingManagerEngine, QGeoServiceProvider, QLocation, 
    QNavigationManager, QPlace, QPlaceAttribute, QPlaceCategory, 
    QPlaceContactDetail, QPlaceContent, QPlaceContentReply, 
    QPlaceContentRequest, QPlaceDetailsReply, QPlaceEditorial, QPlaceIcon, 
    QPlaceIdReply, QPlaceImage, QPlaceManager, QPlaceManagerEngine, 
    QPlaceMatchReply, QPlaceMatchRequest, QPlaceProposedSearchResult, 
    QPlaceRatings, QPlaceReply, QPlaceResult, QPlaceReview, QPlaceSearchReply, 
    QPlaceSearchRequest, QPlaceSearchResult, QPlaceSearchSuggestionReply, 
    QPlaceSupplier, QPlaceUser)

from PyQt5.QtMultimedia import (QAbstractVideoBuffer, QAbstractVideoFilter, 
    QAbstractVideoSurface, QAudio, QAudioBuffer, QAudioDecoder, 
    QAudioDeviceInfo, QAudioEncoderSettings, QAudioFormat, QAudioInput, 
    QAudioOutput, QAudioProbe, QAudioRecorder, QCamera, QCameraExposure, 
    QCameraFocus, QCameraFocusZone, QCameraImageCapture, 
    QCameraImageProcessing, QCameraInfo, QCameraViewfinderSettings, 
    QImageEncoderSettings, QMediaBindableInterface, QMediaContent, 
    QMediaControl, QMediaMetaData, QMediaObject, QMediaPlayer, QMediaPlaylist, 
    QMediaRecorder, QMediaResource, QMediaService, QMediaTimeInterval, 
    QMediaTimeRange, QMultimedia, QRadioData, QRadioTuner, QSound, 
    QSoundEffect, QVideoEncoderSettings, QVideoFilterRunnable, QVideoFrame, 
    QVideoProbe, QVideoSurfaceFormat)

from PyQt5.QtMultimediaWidgets import (QCameraViewfinder, QGraphicsVideoItem, 
    QVideoWidget)

from PyQt5.QtNetwork import (QAbstractNetworkCache, QAbstractSocket, 
    QAuthenticator, QDnsDomainNameRecord, QDnsHostAddressRecord, QDnsLookup, 
    QDnsMailExchangeRecord, QDnsServiceRecord, QDnsTextRecord, QHostAddress, 
    QHostInfo, QHstsPolicy, QHttpMultiPart, QHttpPart, QLocalServer, 
    QLocalSocket, QNetworkAccessManager, QNetworkAddressEntry, 
    QNetworkCacheMetaData, QNetworkConfiguration, 
    QNetworkConfigurationManager, QNetworkCookie, QNetworkCookieJar, 
    QNetworkDatagram, QNetworkDiskCache, QNetworkInterface, QNetworkProxy, 
    QNetworkProxyFactory, QNetworkProxyQuery, QNetworkReply, QNetworkRequest, 
    QNetworkSession, QPasswordDigestor, QSsl, QSslCertificate, 
    QSslCertificateExtension, QSslCipher, QSslConfiguration, 
    QSslDiffieHellmanParameters, QSslEllipticCurve, QSslError, QSslKey, 
    QSslPreSharedKeyAuthenticator, QSslSocket, QTcpServer, QTcpSocket, 
    QUdpSocket)

from PyQt5.QtNetworkAuth import (QAbstractOAuth, QAbstractOAuth2, 
    QAbstractOAuthReplyHandler, QOAuth1, QOAuth1Signature, 
    QOAuth2AuthorizationCodeFlow, QOAuthHttpServerReplyHandler, 
    QOAuthOobReplyHandler)

from PyQt5.QtNfc import (QNdefFilter, QNdefMessage, QNdefNfcIconRecord, 
    QNdefNfcSmartPosterRecord, QNdefNfcTextRecord, QNdefNfcUriRecord, 
    QNdefRecord, QNearFieldManager, QNearFieldShareManager, 
    QNearFieldShareTarget, QNearFieldTarget, QQmlNdefRecord)

from PyQt5.QtOpenGL import QGL, QGLContext, QGLFormat, QGLWidget

from PyQt5.QtPositioning import (QGeoAddress, QGeoAreaMonitorInfo, 
    QGeoAreaMonitorSource, QGeoCircle, QGeoCoordinate, QGeoLocation, QGeoPath, 
    QGeoPolygon, QGeoPositionInfo, QGeoPositionInfoSource, QGeoRectangle, 
    QGeoSatelliteInfo, QGeoSatelliteInfoSource, QGeoShape, 
    QNmeaPositionInfoSource)

from PyQt5.QtPrintSupport import (QAbstractPrintDialog, QPageSetupDialog, 
    QPrintDialog, QPrintEngine, QPrintPreviewDialog, QPrintPreviewWidget, 
    QPrinter, QPrinterInfo)

from PyQt5.QtQml import (QJSEngine, QJSValue, QJSValueIterator, 
    QQmlAbstractUrlInterceptor, QQmlApplicationEngine, QQmlComponent, 
    QQmlContext, QQmlEngine, QQmlError, QQmlExpression, QQmlExtensionPlugin, 
    QQmlFileSelector, QQmlImageProviderBase, QQmlIncubationController, 
    QQmlIncubator, QQmlListProperty, QQmlListReference, 
    QQmlNetworkAccessManagerFactory, QQmlParserStatus, QQmlProperty, 
    QQmlPropertyMap, QQmlPropertyValueSource, QQmlScriptString, qjsEngine, 
    qmlAttachedPropertiesObject, qmlClearTypeRegistrations, 
    qmlRegisterRevision, qmlRegisterSingletonType, qmlRegisterType, 
    qmlRegisterUncreatableType, qmlTypeId)

from PyQt5.QtQuick import (QQuickAsyncImageProvider, QQuickCloseEvent, 
    QQuickFramebufferObject, QQuickImageProvider, QQuickImageResponse, 
    QQuickItem, QQuickItemGrabResult, QQuickPaintedItem, QQuickRenderControl, 
    QQuickTextDocument, QQuickTextureFactory, QQuickView, QQuickWindow, 
    QSGAbstractRenderer, QSGBasicGeometryNode, QSGClipNode, QSGDynamicTexture, 
    QSGEngine, QSGFlatColorMaterial, QSGGeometry, QSGGeometryNode, 
    QSGImageNode, QSGMaterial, QSGMaterialShader, QSGMaterialType, QSGNode, 
    QSGOpacityNode, QSGOpaqueTextureMaterial, QSGRectangleNode, QSGRenderNode, 
    QSGRendererInterface, QSGSimpleRectNode, QSGSimpleTextureNode, QSGTexture, 
    QSGTextureMaterial, QSGTextureProvider, QSGTransformNode, 
    QSGVertexColorMaterial)

from PyQt5.QtQuickWidgets import QQuickWidget

from PyQt5.QtRemoteObjects import (QAbstractItemModelReplica, 
    QRemoteObjectAbstractPersistedStore, QRemoteObjectDynamicReplica, 
    QRemoteObjectHost, QRemoteObjectHostBase, QRemoteObjectNode, 
    QRemoteObjectRegistry, QRemoteObjectRegistryHost, QRemoteObjectReplica, 
    QRemoteObjectSourceLocationInfo, QtRemoteObjects)

from PyQt5.QtSensors import (QAccelerometer, QAccelerometerFilter, 
    QAccelerometerReading, QAltimeter, QAltimeterFilter, QAltimeterReading, 
    QAmbientLightFilter, QAmbientLightReading, QAmbientLightSensor, 
    QAmbientTemperatureFilter, QAmbientTemperatureReading, 
    QAmbientTemperatureSensor, QCompass, QCompassFilter, QCompassReading, 
    QDistanceFilter, QDistanceReading, QDistanceSensor, QGyroscope, 
    QGyroscopeFilter, QGyroscopeReading, QHolsterFilter, QHolsterReading, 
    QHolsterSensor, QHumidityFilter, QHumidityReading, QHumiditySensor, 
    QIRProximityFilter, QIRProximityReading, QIRProximitySensor, QLidFilter, 
    QLidReading, QLidSensor, QLightFilter, QLightReading, QLightSensor, 
    QMagnetometer, QMagnetometerFilter, QMagnetometerReading, 
    QOrientationFilter, QOrientationReading, QOrientationSensor, 
    QPressureFilter, QPressureReading, QPressureSensor, QProximityFilter, 
    QProximityReading, QProximitySensor, QRotationFilter, QRotationReading, 
    QRotationSensor, QSensor, QSensorFilter, QSensorReading, QTapFilter, 
    QTapReading, QTapSensor, QTiltFilter, QTiltReading, QTiltSensor, 
    qoutputrange)

from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

from PyQt5.QtSql import (QSql, QSqlDatabase, QSqlDriver, 
    QSqlDriverCreatorBase, QSqlError, QSqlField, QSqlIndex, QSqlQuery, 
    QSqlQueryModel, QSqlRecord, QSqlRelation, QSqlRelationalDelegate, 
    QSqlRelationalTableModel, QSqlResult, QSqlTableModel)

from PyQt5.QtSvg import (QGraphicsSvgItem, QSvgGenerator, QSvgRenderer, 
    QSvgWidget)

from PyQt5.QtTest import QAbstractItemModelTester, QSignalSpy, QTest

from PyQt5.QtWebChannel import QWebChannel, QWebChannelAbstractTransport

from PyQt5.QtWebSockets import (QMaskGenerator, QWebSocket, 
    QWebSocketCorsAuthenticator, QWebSocketProtocol, QWebSocketServer)

from PyQt5.QtWidgets import (QAbstractButton, QAbstractGraphicsShapeItem, 
    QAbstractItemDelegate, QAbstractItemView, QAbstractScrollArea, 
    QAbstractSlider, QAbstractSpinBox, QAction, QActionGroup, QApplication, 
    QBoxLayout, QButtonGroup, QCalendarWidget, QCheckBox, QColorDialog, 
    QColumnView, QComboBox, QCommandLinkButton, QCommonStyle, QCompleter, 
    QDataWidgetMapper, QDateEdit, QDateTimeEdit, QDesktopWidget, QDial, 
    QDialog, QDialogButtonBox, QDirModel, QDockWidget, QDoubleSpinBox, 
    QErrorMessage, QFileDialog, QFileIconProvider, QFileSystemModel, 
    QFocusFrame, QFontComboBox, QFontDialog, QFormLayout, QFrame, QGesture, 
    QGestureEvent, QGestureRecognizer, QGraphicsAnchor, QGraphicsAnchorLayout, 
    QGraphicsBlurEffect, QGraphicsColorizeEffect, QGraphicsDropShadowEffect, 
    QGraphicsEffect, QGraphicsEllipseItem, QGraphicsGridLayout, QGraphicsItem, 
    QGraphicsItemGroup, QGraphicsLayout, QGraphicsLayoutItem, 
    QGraphicsLineItem, QGraphicsLinearLayout, QGraphicsObject, 
    QGraphicsOpacityEffect, QGraphicsPathItem, QGraphicsPixmapItem, 
    QGraphicsPolygonItem, QGraphicsProxyWidget, QGraphicsRectItem, 
    QGraphicsRotation, QGraphicsScale, QGraphicsScene, 
    QGraphicsSceneContextMenuEvent, QGraphicsSceneDragDropEvent, 
    QGraphicsSceneEvent, QGraphicsSceneHelpEvent, QGraphicsSceneHoverEvent, 
    QGraphicsSceneMouseEvent, QGraphicsSceneMoveEvent, 
    QGraphicsSceneResizeEvent, QGraphicsSceneWheelEvent, 
    QGraphicsSimpleTextItem, QGraphicsTextItem, QGraphicsTransform, 
    QGraphicsView, QGraphicsWidget, QGridLayout, QGroupBox, QHBoxLayout, 
    QHeaderView, QInputDialog, QItemDelegate, QItemEditorCreatorBase, 
    QItemEditorFactory, QKeyEventTransition, QKeySequenceEdit, QLCDNumber, 
    QLabel, QLayout, QLayoutItem, QLineEdit, QListView, QListWidget, 
    QListWidgetItem, QMainWindow, QMdiArea, QMdiSubWindow, QMenu, QMenuBar, 
    QMessageBox, QMouseEventTransition, QOpenGLWidget, QPanGesture, 
    QPinchGesture, QPlainTextDocumentLayout, QPlainTextEdit, QProgressBar, 
    QProgressDialog, QProxyStyle, QPushButton, QRadioButton, QRubberBand, 
    QScrollArea, QScrollBar, QScroller, QScrollerProperties, QShortcut, 
    QSizeGrip, QSizePolicy, QSlider, QSpacerItem, QSpinBox, QSplashScreen, 
    QSplitter, QSplitterHandle, QStackedLayout, QStackedWidget, QStatusBar, 
    QStyle, QStyleFactory, QStyleHintReturn, QStyleHintReturnMask, 
    QStyleHintReturnVariant, QStyleOption, QStyleOptionButton, 
    QStyleOptionComboBox, QStyleOptionComplex, QStyleOptionDockWidget, 
    QStyleOptionFocusRect, QStyleOptionFrame, QStyleOptionGraphicsItem, 
    QStyleOptionGroupBox, QStyleOptionHeader, QStyleOptionMenuItem, 
    QStyleOptionProgressBar, QStyleOptionRubberBand, QStyleOptionSizeGrip, 
    QStyleOptionSlider, QStyleOptionSpinBox, QStyleOptionTab, 
    QStyleOptionTabBarBase, QStyleOptionTabWidgetFrame, QStyleOptionTitleBar, 
    QStyleOptionToolBar, QStyleOptionToolBox, QStyleOptionToolButton, 
    QStyleOptionViewItem, QStylePainter, QStyledItemDelegate, QSwipeGesture, 
    QSystemTrayIcon, QTabBar, QTabWidget, QTableView, QTableWidget, 
    QTableWidgetItem, QTableWidgetSelectionRange, QTapAndHoldGesture, 
    QTapGesture, QTextBrowser, QTextEdit, QTimeEdit, QToolBar, QToolBox, 
    QToolButton, QToolTip, QTreeView, QTreeWidget, QTreeWidgetItem, 
    QTreeWidgetItemIterator, QUndoCommand, QUndoGroup, QUndoStack, QUndoView, 
    QVBoxLayout, QWhatsThis, QWidget, QWidgetAction, QWidgetItem, QWizard, 
    QWizardPage, qApp, qDrawBorderPixmap, qDrawPlainRect, qDrawShadeLine, 
    qDrawShadePanel, qDrawShadeRect, qDrawWinButton, qDrawWinPanel)

from PyQt5.QtWinExtras import (QWinJumpList, QWinJumpListCategory, 
    QWinJumpListItem, QWinTaskbarButton, QWinTaskbarProgress, 
    QWinThumbnailToolBar, QWinThumbnailToolButton, QtWin)

from PyQt5.QtXml import (QDomAttr, QDomCDATASection, QDomCharacterData, 
    QDomComment, QDomDocument, QDomDocumentFragment, QDomDocumentType, 
    QDomElement, QDomEntity, QDomEntityReference, QDomImplementation, 
    QDomNamedNodeMap, QDomNode, QDomNodeList, QDomNotation, 
    QDomProcessingInstruction, QDomText, QXmlAttributes, QXmlContentHandler, 
    QXmlDTDHandler, QXmlDeclHandler, QXmlDefaultHandler, QXmlEntityResolver, 
    QXmlErrorHandler, QXmlInputSource, QXmlLexicalHandler, QXmlLocator, 
    QXmlNamespaceSupport, QXmlParseException, QXmlReader, QXmlSimpleReader)

from PyQt5.QtXmlPatterns import (QAbstractMessageHandler, 
    QAbstractUriResolver, QAbstractXmlNodeModel, QAbstractXmlReceiver, 
    QSimpleXmlNodeModel, QSourceLocation, QXmlFormatter, QXmlItem, QXmlName, 
    QXmlNamePool, QXmlNodeModelIndex, QXmlQuery, QXmlResultItems, QXmlSchema, 
    QXmlSchemaValidator, QXmlSerializer)


# Variables with simple values

PYQT_VERSION = 330755

PYQT_VERSION_STR = '5.12.3'

QT_VERSION = 330760

QT_VERSION_STR = '5.12.8'

QWIDGETSIZE_MAX = 16777215

# no functions
# no classes
# variables with complex values

PYQT_CONFIGURATION = {
    'sip_flags': '-n PyQt5.sip -t WS_WIN -t Qt_5_12_8',
}




