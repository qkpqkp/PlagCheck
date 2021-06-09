# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QLocale(__sip.simplewrapper):
    """
    QLocale()
    QLocale(str)
    QLocale(QLocale.Language, country: QLocale.Country = QLocale.AnyCountry)
    QLocale(QLocale)
    QLocale(QLocale.Language, QLocale.Script, QLocale.Country)
    """
    def amText(self): # real signature unknown; restored from __doc__
        """ amText(self) -> str """
        return ""

    def bcp47Name(self): # real signature unknown; restored from __doc__
        """ bcp47Name(self) -> str """
        return ""

    def c(self): # real signature unknown; restored from __doc__
        """ c() -> QLocale """
        return QLocale

    def country(self): # real signature unknown; restored from __doc__
        """ country(self) -> QLocale.Country """
        pass

    def countryToString(self, QLocale_Country): # real signature unknown; restored from __doc__
        """ countryToString(QLocale.Country) -> str """
        return ""

    def createSeparatedList(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ createSeparatedList(self, Iterable[str]) -> str """
        return ""

    def currencySymbol(self, format=None): # real signature unknown; restored from __doc__
        """ currencySymbol(self, format: QLocale.CurrencySymbolFormat = QLocale.CurrencySymbol) -> str """
        return ""

    def dateFormat(self, format=None): # real signature unknown; restored from __doc__
        """ dateFormat(self, format: QLocale.FormatType = QLocale.LongFormat) -> str """
        return ""

    def dateTimeFormat(self, format=None): # real signature unknown; restored from __doc__
        """ dateTimeFormat(self, format: QLocale.FormatType = QLocale.LongFormat) -> str """
        return ""

    def dayName(self, p_int, format=None): # real signature unknown; restored from __doc__
        """ dayName(self, int, format: QLocale.FormatType = QLocale.LongFormat) -> str """
        return ""

    def decimalPoint(self): # real signature unknown; restored from __doc__
        """ decimalPoint(self) -> str """
        return ""

    def exponential(self): # real signature unknown; restored from __doc__
        """ exponential(self) -> str """
        return ""

    def firstDayOfWeek(self): # real signature unknown; restored from __doc__
        """ firstDayOfWeek(self) -> Qt.DayOfWeek """
        pass

    def formattedDataSize(self, p_int, precision=2, format, QLocale_DataSizeFormats=None, QLocale_DataSizeFormat=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ formattedDataSize(self, int, precision: int = 2, format: Union[QLocale.DataSizeFormats, QLocale.DataSizeFormat] = QLocale.DataSizeIecFormat) -> str """
        pass

    def groupSeparator(self): # real signature unknown; restored from __doc__
        """ groupSeparator(self) -> str """
        return ""

    def language(self): # real signature unknown; restored from __doc__
        """ language(self) -> QLocale.Language """
        pass

    def languageToString(self, QLocale_Language): # real signature unknown; restored from __doc__
        """ languageToString(QLocale.Language) -> str """
        return ""

    def matchingLocales(self, QLocale_Language, QLocale_Script, QLocale_Country): # real signature unknown; restored from __doc__
        """ matchingLocales(QLocale.Language, QLocale.Script, QLocale.Country) -> List[QLocale] """
        return []

    def measurementSystem(self): # real signature unknown; restored from __doc__
        """ measurementSystem(self) -> QLocale.MeasurementSystem """
        pass

    def monthName(self, p_int, format=None): # real signature unknown; restored from __doc__
        """ monthName(self, int, format: QLocale.FormatType = QLocale.LongFormat) -> str """
        return ""

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def nativeCountryName(self): # real signature unknown; restored from __doc__
        """ nativeCountryName(self) -> str """
        return ""

    def nativeLanguageName(self): # real signature unknown; restored from __doc__
        """ nativeLanguageName(self) -> str """
        return ""

    def negativeSign(self): # real signature unknown; restored from __doc__
        """ negativeSign(self) -> str """
        return ""

    def numberOptions(self): # real signature unknown; restored from __doc__
        """ numberOptions(self) -> QLocale.NumberOptions """
        pass

    def percent(self): # real signature unknown; restored from __doc__
        """ percent(self) -> str """
        return ""

    def pmText(self): # real signature unknown; restored from __doc__
        """ pmText(self) -> str """
        return ""

    def positiveSign(self): # real signature unknown; restored from __doc__
        """ positiveSign(self) -> str """
        return ""

    def quoteString(self, p_str, style=None): # real signature unknown; restored from __doc__
        """ quoteString(self, str, style: QLocale.QuotationStyle = QLocale.StandardQuotation) -> str """
        return ""

    def script(self): # real signature unknown; restored from __doc__
        """ script(self) -> QLocale.Script """
        pass

    def scriptToString(self, QLocale_Script): # real signature unknown; restored from __doc__
        """ scriptToString(QLocale.Script) -> str """
        return ""

    def setDefault(self, QLocale): # real signature unknown; restored from __doc__
        """ setDefault(QLocale) """
        pass

    def setNumberOptions(self, Union, QLocale_NumberOptions=None, QLocale_NumberOption=None): # real signature unknown; restored from __doc__
        """ setNumberOptions(self, Union[QLocale.NumberOptions, QLocale.NumberOption]) """
        pass

    def standaloneDayName(self, p_int, format=None): # real signature unknown; restored from __doc__
        """ standaloneDayName(self, int, format: QLocale.FormatType = QLocale.LongFormat) -> str """
        return ""

    def standaloneMonthName(self, p_int, format=None): # real signature unknown; restored from __doc__
        """ standaloneMonthName(self, int, format: QLocale.FormatType = QLocale.LongFormat) -> str """
        return ""

    def swap(self, QLocale): # real signature unknown; restored from __doc__
        """ swap(self, QLocale) """
        pass

    def system(self): # real signature unknown; restored from __doc__
        """ system() -> QLocale """
        return QLocale

    def textDirection(self): # real signature unknown; restored from __doc__
        """ textDirection(self) -> Qt.LayoutDirection """
        pass

    def timeFormat(self, format=None): # real signature unknown; restored from __doc__
        """ timeFormat(self, format: QLocale.FormatType = QLocale.LongFormat) -> str """
        return ""

    def toCurrencyString(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toCurrencyString(self, float, symbol: str = '') -> str
        toCurrencyString(self, float, str, int) -> str
        toCurrencyString(self, int, symbol: str = '') -> str
        """
        return ""

    def toDate(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toDate(self, str, format: QLocale.FormatType = QLocale.LongFormat) -> QDate
        toDate(self, str, str) -> QDate
        """
        return QDate

    def toDateTime(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toDateTime(self, str, format: QLocale.FormatType = QLocale.LongFormat) -> QDateTime
        toDateTime(self, str, str) -> QDateTime
        """
        return QDateTime

    def toDouble(self, p_str): # real signature unknown; restored from __doc__
        """ toDouble(self, str) -> Tuple[float, bool] """
        pass

    def toFloat(self, p_str): # real signature unknown; restored from __doc__
        """ toFloat(self, str) -> Tuple[float, bool] """
        pass

    def toInt(self, p_str): # real signature unknown; restored from __doc__
        """ toInt(self, str) -> Tuple[int, bool] """
        pass

    def toLongLong(self, p_str): # real signature unknown; restored from __doc__
        """ toLongLong(self, str) -> Tuple[int, bool] """
        pass

    def toLower(self, p_str): # real signature unknown; restored from __doc__
        """ toLower(self, str) -> str """
        return ""

    def toShort(self, p_str): # real signature unknown; restored from __doc__
        """ toShort(self, str) -> Tuple[int, bool] """
        pass

    def toString(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toString(self, float, format: str = 'g', precision: int = 6) -> str
        toString(self, Union[QDateTime, datetime.datetime], str) -> str
        toString(self, Union[QDateTime, datetime.datetime], format: QLocale.FormatType = QLocale.LongFormat) -> str
        toString(self, Union[QDate, datetime.date], str) -> str
        toString(self, Union[QDate, datetime.date], format: QLocale.FormatType = QLocale.LongFormat) -> str
        toString(self, Union[QTime, datetime.time], str) -> str
        toString(self, Union[QTime, datetime.time], format: QLocale.FormatType = QLocale.LongFormat) -> str
        toString(self, int) -> str
        """
        return ""

    def toTime(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toTime(self, str, format: QLocale.FormatType = QLocale.LongFormat) -> QTime
        toTime(self, str, str) -> QTime
        """
        return QTime

    def toUInt(self, p_str): # real signature unknown; restored from __doc__
        """ toUInt(self, str) -> Tuple[int, bool] """
        pass

    def toULongLong(self, p_str): # real signature unknown; restored from __doc__
        """ toULongLong(self, str) -> Tuple[int, bool] """
        pass

    def toUpper(self, p_str): # real signature unknown; restored from __doc__
        """ toUpper(self, str) -> str """
        return ""

    def toUShort(self, p_str): # real signature unknown; restored from __doc__
        """ toUShort(self, str) -> Tuple[int, bool] """
        pass

    def uiLanguages(self): # real signature unknown; restored from __doc__
        """ uiLanguages(self) -> List[str] """
        return []

    def weekdays(self): # real signature unknown; restored from __doc__
        """ weekdays(self) -> List[Qt.DayOfWeek] """
        return []

    def zeroDigit(self): # real signature unknown; restored from __doc__
        """ zeroDigit(self) -> str """
        return ""

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Abkhazian = 2
    AdlamScript = 134
    Afan = 3
    Afar = 4
    Afghanistan = 1
    Afrikaans = 5
    Aghem = 237
    Ahom = 340
    AhomScript = 128
    Akan = 146
    Akkadian = 262
    Akoose = 312
    AlandIslands = 248
    Albania = 2
    Albanian = 6
    Algeria = 3
    AlternateQuotation = 1
    AmericanSamoa = 4
    AmericanSignLanguage = 341
    Amharic = 7
    AnatolianHieroglyphsScript = 129
    AncientEgyptian = 263
    AncientGreek = 264
    AncientNorthArabian = 331
    Andorra = 5
    Angola = 6
    Anguilla = 7
    Antarctica = 8
    AntiguaAndBarbuda = 9
    AnyCountry = 0
    AnyLanguage = 0
    AnyScript = 0
    Arabic = 8
    ArabicScript = 1
    Aragonese = 261
    Aramaic = 265
    ArdhamagadhiPrakrit = 342
    Argentina = 10
    Armenia = 11
    Armenian = 9
    ArmenianScript = 10
    Aruba = 12
    AscensionIsland = 247
    Assamese = 10
    Asturian = 256
    Asu = 205
    Atsam = 156
    Australia = 13
    Austria = 14
    Avaric = 216
    Avestan = 255
    AvestanScript = 36
    Aymara = 11
    Azerbaijan = 15
    Azerbaijani = 12
    Bafia = 243
    Bahamas = 16
    Bahrain = 17
    Balinese = 266
    BalineseScript = 37
    Bambara = 188
    BamumScript = 38
    Bamun = 267
    Bangladesh = 18
    Barbados = 19
    Basaa = 238
    Bashkir = 13
    Basque = 14
    Bassa = 336
    BassaVahScript = 106
    BatakScript = 39
    BatakToba = 268
    Belarus = 20
    Belarusian = 22
    Belgium = 21
    Belize = 22
    Bemba = 195
    Bena = 186
    Bengali = 15
    BengaliScript = 11
    Benin = 23
    Bermuda = 24
    BhaiksukiScript = 135
    Bhojpuri = 343
    Bhutan = 25
    Bhutani = 16
    Bihari = 17
    Bislama = 18
    Blin = 152
    Bodo = 215
    Bolivia = 26
    Bonaire = 255
    BopomofoScript = 40
    BosniaAndHerzegowina = 27
    Bosnian = 142
    Botswana = 28
    BouvetIsland = 29
    BrahmiScript = 41
    BrailleScript = 103
    Brazil = 30
    Breton = 19
    BritishIndianOceanTerritory = 31
    BritishVirginIslands = 233
    Brunei = 32
    Buginese = 269
    BugineseScript = 42
    Buhid = 270
    BuhidScript = 43
    Bulgaria = 33
    Bulgarian = 20
    BurkinaFaso = 34
    Burmese = 21
    Burundi = 35
    Byelorussian = 22
    C = 1
    Cambodia = 36
    Cambodian = 23
    Cameroon = 37
    Canada = 38
    CanadianAboriginalScript = 44
    CanaryIslands = 238
    Cantonese = 357
    CapeVerde = 39
    Carian = 271
    CarianScript = 45
    Catalan = 24
    CaucasianAlbanianScript = 105
    CaymanIslands = 40
    CentralAfricanRepublic = 41
    CentralKurdish = 316
    CentralMoroccoTamazight = 212
    CeutaAndMelilla = 250
    Chad = 42
    Chakma = 272
    ChakmaScript = 46
    Chamorro = 217
    ChamScript = 47
    Chechen = 218
    Cherokee = 190
    CherokeeScript = 12
    Chewa = 165
    Chiga = 211
    Chile = 43
    China = 44
    Chinese = 25
    ChristmasIsland = 45
    Church = 219
    Chuvash = 220
    ClassicalMandaic = 273
    ClippertonIsland = 241
    CocosIslands = 46
    Colognian = 201
    Colombia = 47
    Comoros = 48
    CongoBrazzaville = 50
    CongoKinshasa = 49
    CongoSwahili = 250
    CookIslands = 51
    Coptic = 274
    CopticScript = 48
    Cornish = 145
    Corsican = 26
    CostaRica = 52
    Cree = 221
    Croatia = 54
    Croatian = 27
    Cuba = 55
    CuneiformScript = 94
    CuraSao = 152
    CurrencyDisplayName = 2
    CurrencyIsoCode = 0
    CurrencySymbol = 1
    CypriotScript = 49
    Cyprus = 56
    CyrillicScript = 2
    Czech = 28
    CzechRepublic = 57
    Danish = 29
    DataSizeIecFormat = 0
    DataSizeSIFormat = 3
    DataSizeTraditionalFormat = 2
    DefaultNumberOptions = 0
    DemocraticRepublicOfCongo = 49
    DemocraticRepublicOfKorea = 113
    Denmark = 58
    DeseretScript = 3
    DevanagariScript = 13
    DiegoGarcia = 249
    Divehi = 143
    Djibouti = 59
    Dogri = 275
    Dominica = 60
    DominicanRepublic = 61
    Duala = 240
    DuployanScript = 107
    Dutch = 30
    Dzongkha = 16
    EasternCham = 276
    EasternKayah = 277
    EastTimor = 62
    Ecuador = 63
    Egypt = 64
    EgyptianHieroglyphsScript = 50
    ElbasanScript = 108
    ElSalvador = 65
    Embu = 189
    English = 31
    EquatorialGuinea = 66
    Eritrea = 67
    Esperanto = 32
    Estonia = 68
    Estonian = 33
    Ethiopia = 69
    EthiopicScript = 14
    Etruscan = 278
    Europe = 261
    EuropeanUnion = 258
    Ewe = 161
    Ewondo = 242
    FalklandIslands = 70
    FaroeIslands = 71
    Faroese = 34
    Fiji = 72
    Fijian = 35
    Filipino = 166
    Finland = 73
    Finnish = 36
    FloatingPointShortest = -128
    France = 74
    FraserScript = 51
    French = 37
    FrenchGuiana = 76
    FrenchPolynesia = 77
    FrenchSouthernTerritories = 78
    Frisian = 38
    Friulian = 159
    Fulah = 177
    Ga = 148
    Gabon = 79
    Gaelic = 39
    Galician = 40
    Gambia = 80
    Ganda = 194
    Geez = 153
    Georgia = 81
    Georgian = 41
    GeorgianScript = 15
    German = 42
    Germany = 82
    Ghana = 83
    Gibraltar = 84
    GlagoliticScript = 52
    Gothic = 279
    GothicScript = 53
    GranthaScript = 109
    Greece = 85
    Greek = 43
    GreekScript = 16
    Greenland = 86
    Greenlandic = 44
    Grenada = 87
    Guadeloupe = 88
    Guam = 89
    Guarani = 45
    Guatemala = 90
    Guernsey = 75
    Guinea = 91
    GuineaBissau = 92
    Gujarati = 46
    GujaratiScript = 17
    GurmukhiScript = 4
    Gusii = 175
    Guyana = 93
    Haiti = 94
    Haitian = 222
    HangulScript = 55
    HanScript = 54
    Hanunoo = 280
    HanunooScript = 56
    HanWithBopomofoScript = 140
    HatranScript = 130
    Hausa = 47
    Hawaiian = 163
    HeardAndMcDonaldIslands = 95
    Hebrew = 48
    HebrewScript = 18
    Herero = 223
    HieroglyphicLuwian = 344
    Hindi = 49
    HiraganaScript = 104
    HiriMotu = 224
    HmongNjua = 333
    Ho = 334
    Honduras = 96
    HongKong = 97
    Hungarian = 50
    Hungary = 98
    Iceland = 99
    Icelandic = 51
    Igbo = 149
    ImperialAramaicScript = 57
    ImperialSystem = 1
    ImperialUKSystem = 2
    ImperialUSSystem = 1
    InariSami = 326
    IncludeTrailingZeroesAfterDot = 16
    India = 100
    Indonesia = 101
    Indonesian = 52
    Ingush = 281
    InscriptionalPahlaviScript = 58
    InscriptionalParthianScript = 59
    Interlingua = 53
    Interlingue = 54
    Inuktitut = 55
    Inupiak = 56
    Iran = 102
    Iraq = 103
    Ireland = 104
    Irish = 57
    IsleOfMan = 251
    Israel = 105
    Italian = 58
    Italy = 106
    IvoryCoast = 53
    Jamaica = 107
    JamoScript = 141
    Japan = 108
    Japanese = 59
    JapaneseScript = 19
    Javanese = 60
    JavaneseScript = 60
    Jersey = 252
    Jju = 158
    JolaFonyi = 241
    Jordan = 109
    Kabuverdianu = 196
    Kabyle = 184
    KaithiScript = 61
    Kako = 258
    Kalenjin = 198
    Kamba = 150
    Kannada = 61
    KannadaScript = 21
    Kanuri = 225
    Kashmiri = 62
    KatakanaScript = 62
    KayahLiScript = 63
    Kazakh = 63
    Kazakhstan = 110
    Kenya = 111
    Kenyang = 319
    KharoshthiScript = 64
    Khmer = 23
    KhmerScript = 20
    KhojkiScript = 111
    KhudawadiScript = 125
    Kiche = 323
    Kikuyu = 178
    Kinyarwanda = 64
    Kirghiz = 65
    Kiribati = 112
    Komi = 226
    Kongo = 227
    Konkani = 147
    Korean = 66
    KoreanScript = 22
    Koro = 154
    Kosovo = 257
    KoyraboroSenni = 213
    KoyraChiini = 208
    Kpelle = 169
    Kurdish = 67
    Kurundi = 68
    Kuwait = 115
    Kwanyama = 228
    Kwasio = 246
    Kyrgyzstan = 116
    Lakota = 313
    Langi = 193
    LannaScript = 65
    Lao = 69
    Laos = 117
    LaoScript = 23
    LargeFloweryMiao = 282
    LastCountry = 261
    LastLanguage = 359
    Latin = 70
    LatinAmerica = 246
    LatinAmericaAndTheCaribbean = 246
    LatinScript = 7
    Latvia = 118
    Latvian = 71
    Lebanon = 119
    Lepcha = 283
    LepchaScript = 66
    Lesotho = 120
    Lezghian = 335
    Liberia = 121
    Libya = 122
    Liechtenstein = 123
    Limbu = 284
    Limburgish = 229
    LimbuScript = 67
    LinearA = 332
    LinearAScript = 112
    LinearBScript = 68
    Lingala = 72
    Lisu = 285
    LiteraryChinese = 345
    Lithuania = 124
    Lithuanian = 73
    LongFormat = 0
    LowerSorbian = 317
    LowGerman = 170
    Lu = 286
    LubaKatanga = 230
    LuleSami = 325
    Luo = 210
    Luxembourg = 125
    Luxembourgish = 231
    Luyia = 204
    Lycian = 287
    LycianScript = 69
    Lydian = 288
    LydianScript = 70
    Macau = 126
    Macedonia = 127
    Macedonian = 74
    Machame = 200
    Madagascar = 128
    MahajaniScript = 113
    Maithili = 339
    MakhuwaMeetto = 244
    Makonde = 192
    Malagasy = 75
    Malawi = 129
    Malay = 76
    Malayalam = 77
    MalayalamScript = 24
    Malaysia = 130
    Maldives = 131
    Mali = 132
    Malta = 133
    Maltese = 78
    MandaeanScript = 71
    Mandingo = 289
    ManichaeanMiddlePersian = 329
    ManichaeanScript = 114
    Manipuri = 290
    Manx = 144
    Maori = 79
    Mapuche = 315
    Marathi = 80
    MarchenScript = 136
    Marshallese = 81
    MarshallIslands = 134
    Martinique = 135
    Masai = 202
    Mauritania = 136
    Mauritius = 137
    Mayotte = 138
    Mazanderani = 346
    MeiteiMayekScript = 72
    Mende = 330
    MendeKikakuiScript = 115
    Meroitic = 291
    MeroiticCursiveScript = 74
    MeroiticScript = 73
    Meru = 197
    Meta = 259
    MetricSystem = 0
    Mexico = 139
    Micronesia = 140
    ModiScript = 116
    Mohawk = 320
    Moldavian = 95
    Moldova = 141
    Monaco = 142
    Mongolia = 143
    Mongolian = 82
    MongolianScript = 8
    Mono = 337
    Montenegro = 242
    Montserrat = 144
    Morisyen = 191
    Morocco = 145
    Mozambique = 146
    MroScript = 117
    Mru = 347
    MultaniScript = 131
    Mundang = 245
    Myanmar = 147
    MyanmarScript = 25
    NabataeanScript = 119
    Nama = 199
    Namibia = 148
    NarrowFormat = 2
    NauruCountry = 149
    NauruLanguage = 83
    Navaho = 232
    Ndonga = 233
    Nepal = 150
    Nepali = 84
    Netherlands = 151
    Newari = 348
    NewaScript = 137
    NewCaledonia = 153
    NewTaiLueScript = 76
    NewZealand = 154
    Ngiemboon = 260
    Ngomba = 257
    Nicaragua = 155
    Niger = 156
    Nigeria = 157
    Niue = 158
    Nko = 321
    NkoScript = 75
    NorfolkIsland = 159
    NorthernLuri = 349
    NorthernMarianaIslands = 160
    NorthernSami = 173
    NorthernSotho = 172
    NorthernThai = 292
    NorthKorea = 113
    NorthNdebele = 181
    Norway = 161
    Norwegian = 85
    NorwegianBokmal = 85
    NorwegianNynorsk = 141
    Nuer = 247
    Nyanja = 165
    Nyankole = 185
    Occitan = 86
    OghamScript = 77
    Ojibwa = 234
    OlChikiScript = 78
    OldHungarianScript = 132
    OldIrish = 293
    OldItalicScript = 79
    OldNorse = 294
    OldNorthArabianScript = 118
    OldPermicScript = 122
    OldPersian = 295
    OldPersianScript = 80
    OldSouthArabianScript = 81
    OldTurkish = 296
    Oman = 162
    OmitGroupSeparator = 1
    OmitLeadingZeroInExponent = 4
    Oriya = 87
    OriyaScript = 26
    OrkhonScript = 82
    Oromo = 3
    Osage = 358
    OsageScript = 138
    OsmanyaScript = 83
    Ossetic = 101
    OutlyingOceania = 259
    PahawhHmongScript = 110
    Pahlavi = 297
    Pakistan = 163
    Palau = 164
    Palauan = 350
    PalestinianTerritories = 165
    Pali = 235
    PalmyreneScript = 120
    Panama = 166
    Papiamento = 351
    PapuaNewGuinea = 167
    Paraguay = 168
    Parthian = 298
    Pashto = 88
    PauCinHauScript = 121
    PeoplesRepublicOfCongo = 50
    Persian = 89
    Peru = 169
    PhagsPaScript = 84
    Philippines = 170
    Phoenician = 299
    PhoenicianScript = 85
    Pitcairn = 171
    Poland = 172
    Polish = 90
    PollardPhoneticScript = 86
    Portugal = 173
    Portuguese = 91
    PrakritLanguage = 300
    Prussian = 322
    PsalterPahlaviScript = 123
    PuertoRico = 174
    Punjabi = 92
    Qatar = 175
    Quechua = 93
    Rejang = 301
    RejangScript = 87
    RejectGroupSeparator = 2
    RejectLeadingZeroInExponent = 8
    RejectTrailingZeroesAfterDot = 32
    RepublicOfKorea = 114
    Reunion = 176
    RhaetoRomance = 94
    Romania = 177
    Romanian = 95
    Romansh = 94
    Rombo = 182
    Rundi = 68
    RunicScript = 88
    Russia = 178
    Russian = 96
    RussianFederation = 178
    Rwa = 209
    Rwanda = 179
    Sabaean = 302
    Saho = 207
    SaintBarthelemy = 244
    SaintHelena = 199
    SaintKittsAndNevis = 180
    SaintLucia = 181
    SaintMartin = 245
    SaintPierreAndMiquelon = 200
    SaintVincentAndTheGrenadines = 182
    Sakha = 248
    Samaritan = 303
    SamaritanScript = 89
    Samburu = 179
    Samoa = 183
    Samoan = 97
    Sango = 98
    Sangu = 249
    SanMarino = 184
    Sanskrit = 99
    Santali = 304
    SaoTomeAndPrincipe = 185
    Saraiki = 352
    Sardinian = 115
    SaudiArabia = 186
    Saurashtra = 305
    SaurashtraScript = 90
    Sena = 180
    Senegal = 187
    Serbia = 243
    Serbian = 100
    SerboCroatian = 100
    Seychelles = 188
    Shambala = 214
    SharadaScript = 91
    ShavianScript = 92
    Shona = 104
    ShortFormat = 1
    SichuanYi = 168
    Sidamo = 155
    SiddhamScript = 124
    SierraLeone = 189
    SignWritingScript = 133
    SimplifiedChineseScript = 5
    SimplifiedHanScript = 5
    Sindhi = 105
    Singapore = 190
    Sinhala = 106
    SinhalaScript = 32
    SintMaarten = 256
    SkoltSami = 327
    Slovak = 108
    Slovakia = 191
    Slovenia = 192
    Slovenian = 109
    Soga = 203
    SolomonIslands = 193
    Somali = 110
    Somalia = 194
    Sora = 306
    SoraSompengScript = 93
    SouthAfrica = 195
    SouthernSami = 324
    SouthernSotho = 102
    SouthGeorgiaAndTheSouthSandwichIslands = 196
    SouthKorea = 114
    SouthNdebele = 171
    SouthSudan = 254
    Spain = 197
    Spanish = 111
    SriLanka = 198
    StandardMoroccanTamazight = 314
    StandardQuotation = 0
    Sudan = 201
    Sundanese = 112
    SundaneseScript = 95
    Suriname = 202
    SvalbardAndJanMayenIslands = 203
    Swahili = 113
    Swati = 107
    Swaziland = 204
    Sweden = 205
    Swedish = 114
    SwissGerman = 167
    Switzerland = 206
    Sylheti = 307
    SylotiNagriScript = 96
    Syria = 207
    Syriac = 151
    SyriacScript = 33
    SyrianArabRepublic = 207
    Tachelhit = 183
    Tagalog = 166
    TagalogScript = 97
    Tagbanwa = 308
    TagbanwaScript = 98
    Tahitian = 127
    TaiDam = 309
    TaiLeScript = 99
    TaiNua = 310
    Taita = 176
    TaiVietScript = 100
    Taiwan = 208
    Tajik = 116
    Tajikistan = 209
    TakriScript = 101
    Tamil = 117
    TamilScript = 27
    Tangut = 359
    TangutScript = 139
    Tanzania = 210
    Taroko = 174
    Tasawaq = 251
    Tatar = 118
    TedimChin = 338
    Telugu = 119
    TeluguScript = 28
    Teso = 206
    ThaanaScript = 29
    Thai = 120
    Thailand = 211
    ThaiScript = 30
    Tibetan = 121
    TibetanScript = 31
    TifinaghScript = 9
    Tigre = 157
    Tigrinya = 122
    TirhutaScript = 126
    Togo = 212
    Tokelau = 213
    TokelauCountry = 213
    TokelauLanguage = 353
    TokPisin = 354
    Tonga = 214
    Tongan = 123
    TraditionalChineseScript = 6
    TraditionalHanScript = 6
    TrinidadAndTobago = 215
    TristanDaCunha = 253
    Tsonga = 124
    Tswana = 103
    Tunisia = 216
    Turkey = 217
    Turkish = 125
    Turkmen = 126
    Turkmenistan = 218
    TurksAndCaicosIslands = 219
    Tuvalu = 220
    TuvaluCountry = 220
    TuvaluLanguage = 355
    Twi = 146
    Tyap = 164
    Uganda = 221
    Ugaritic = 311
    UgariticScript = 102
    Uighur = 128
    Uigur = 128
    Ukraine = 222
    Ukrainian = 129
    UncodedLanguages = 356
    UnitedArabEmirates = 223
    UnitedKingdom = 224
    UnitedStates = 225
    UnitedStatesMinorOutlyingIslands = 226
    UnitedStatesVirginIslands = 234
    UpperSorbian = 318
    Urdu = 130
    Uruguay = 227
    Uzbek = 131
    Uzbekistan = 228
    Vai = 252
    VaiScript = 35
    Vanuatu = 229
    VarangKshitiScript = 127
    VaticanCityState = 230
    Venda = 160
    Venezuela = 231
    Vietnam = 232
    Vietnamese = 132
    Volapuk = 133
    Vunjo = 187
    Walamo = 162
    WallisAndFutunaIslands = 235
    Walloon = 236
    Walser = 253
    Warlpiri = 328
    Welsh = 134
    WesternFrisian = 38
    WesternSahara = 236
    Wolof = 135
    World = 260
    Xhosa = 136
    Yangben = 254
    Yemen = 237
    Yiddish = 137
    YiScript = 34
    Yoruba = 138
    Zambia = 239
    Zarma = 239
    Zhuang = 139
    Zimbabwe = 240
    Zulu = 140


