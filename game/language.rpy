default russian_selected = False

screen language_select():
    tag menu
    
    add "gui/menu_bg.png"
    
    vbox:
        style_prefix "language_select"
        xpos 150
        yalign 0.35

        text "Select Language" size 50 color "#ffffff" outlines [(4, "#000000", 1, 1)] xpos -20 ypos -25

        viewport:
            id "language_viewport"
            draggable True
            mousewheel True
            ymaximum 800  

            vbox:
                spacing 10

                textbutton "English":
                    action Language(None)  
                    at choice_hover
                    style "language_button"
                        
                textbutton "Spanish":
                    action Language("spanish")
                    at choice_hover
                    style "language_button"
                        
                textbutton "Russian":
                    action Language("russian")
                    at choice_hover
                    style "language_button"
                        
                textbutton "German":
                    action Language("german")
                    at choice_hover
                    style "language_button"
                        
                textbutton "Japanese":
                    action Language("japanese")
                    at choice_hover
                    style "language_button"
                        
                textbutton "Turkish":
                    action Language("turkish")
                    at choice_hover
                    style "language_button"
                        
                textbutton "Chinese (Simplified)":
                    action Language("chinese_simplified")
                    at choice_hover
                    style "language_button"
                        
                textbutton "Chinese (Traditional)":
                    action Language("chinese_traditional")
                    at choice_hover
                    style "language_button"
                        
                textbutton "Portuguese":
                    action Language("portuguese")
                    at choice_hover
                    style "language_button"
                        
                textbutton "French":
                    action Language("french")
                    at choice_hover
                    style "language_button"

                textbutton "Korean":
                    action Language("korean")
                    at choice_hover
                    style "language_button" 
                
                textbutton "Czech":
                    action Language("czech")
                    at choice_hover
                    style "language_button"
                
                textbutton "Dutch":
                    action Language("dutch")
                    at choice_hover
                    style "language_button"
                
                textbutton "Hindi":
                    action Language("hindi")
                    at choice_hover
                    style "language_button"
                
                textbutton "Italian":
                    action Language("italian")
                    at choice_hover
                    style "language_button"
                
                textbutton "Polish":
                    action Language("polish")
                    at choice_hover
                    style "language_button"

                textbutton "Thai":
                    action Language("thai")
                    at choice_hover
                    style "language_button"

                textbutton "Vietnamese":
                    action Language("vietnamese")
                    at choice_hover
                    style "language_button"

                textbutton "Ukrainian":
                    action Language("ukrainian")
                    at choice_hover
                    style "language_button"

                textbutton "Indonesian":
                    action Language("indonesian")
                    at choice_hover
                    style "language_button"

                textbutton "Arabic":
                    action Language("arabic")
                    at choice_hover
                    style "language_button" 

    vbox:        
        xmaximum 1100
        ymaximum 600
        xalign 0.84
        yalign 0.45
        spacing 50
        if renpy.game.preferences.language == "spanish":
            text "Las traducciones se generan mediante inteligencia artificial. Puede haber errores, traducciones incorrectas o traducciones vacías." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]  
            text "Si desea corregir alguna traducción o sugerir idiomas adicionales, únase al servidor de {a=https://discord.gg/u9GwfyjJNs}{image=gui/discord_32.png} Discord{/a}." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)] 
        elif renpy.game.preferences.language == "Russiann":
            text "Переводы создаются с помощью искусственного интеллекта. Возможны ошибки, неправильные переводы или пустые переводы." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)] 
            text "Если вы хотите исправить переводы или предложить дополнительные языки, присоединяйтесь к серверу {a=https://discord.gg/u9GwfyjJNs}{image=gui/discord_32.png} Discord{/a}." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)] 
        elif renpy.game.preferences.language == "german":
            text "Übersetzungen werden mithilfe von künstlicher Intelligenz generiert. Es können Fehler, Fehlübersetzungen oder leere Übersetzungen auftreten." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)] 
            text "Wenn Sie Übersetzungen korrigieren oder zusätzliche Sprachen vorschlagen möchten, treten Sie dem {a=https://discord.gg/u9GwfyjJNs}{image=gui/discord_32.png} Discord{/a}-Server bei." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)] 
        elif renpy.game.preferences.language == "japanese":
            text "翻訳は人工知能を使用して生成されます。誤り、不正確な翻訳、または空白の翻訳が含まれる場合があります。" size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)] 
            text "翻訳を修正したり追加の言語を提案したい場合は、{a=https://discord.gg/u9GwfyjJNs}{image=gui/discord_32.png} Discord{/a}サーバーに参加してください。" size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)] 
        elif renpy.game.preferences.language == "turkish":
            text "Çeviriler yapay zeka kullanılarak oluşturulmuştur. Hatalar, yanlış çeviriler veya boş çeviriler olabilir." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)] 
            text "Herhangi bir çeviriyi düzeltmek veya ek diller önermek isterseniz, {a=https://discord.gg/u9GwfyjJNs}{image=gui/discord_32.png} Discord{/a} sunucusuna katılın." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]
        elif renpy.game.preferences.language == "chinese_simplified":
            text "翻译是使用人工智能生成的。 可能存在错误、误译或空白翻译。" size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)] 
            text "如果您想纠正任何翻译或建议其他语言，请加入 {a=https://discord.gg/u9GwfyjJNs}{image=gui/discord_32.png} Discord{/a} 服务器。" size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)] 
        elif renpy.game.preferences.language == "chinese_traditional":
            text "翻譯是使用人工智能生成的。 可能存在錯誤、誤譯或空白翻譯。" size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)] 
            text "如果您想糾正任何翻譯或建議其他語言，請加入 {a=https://discord.gg/u9GwfyjJNs}{image=gui/discord_32.png} Discord{/a} 服務器。" size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)] 
        elif renpy.game.preferences.language == "portuguese":
            text "As traduções são geradas usando inteligência artificial. Podem haver erros, traduções incorretas ou traduções vazias." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)] 
            text "Se você quiser corrigir alguma tradução ou sugerir idiomas adicionais, por favor, junte-se ao servidor do {a=https://discord.gg/u9GwfyjJNs}{image=gui/discord_32.png} Discord{/a}." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)] 
        elif renpy.game.preferences.language == "french":
            text "Les traductions sont générées à l'aide de l'intelligence artificielle. Il peut y avoir des erreurs, des mauvaises traductions ou des traductions vides." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)] 
            text "Si vous souhaitez corriger des traductions ou suggérer des langues supplémentaires, veuillez rejoindre le serveur {a=https://discord.gg/u9GwfyjJNs}{image=gui/discord_32.png} Discord{/a}." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]
        #hop
        elif renpy.game.preferences.language == "czech":
            text "Překlady jsou generovány pomocí umělé inteligence. Mohou se vyskytnout chyby, špatné překlady nebo prázdné překlady." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]
            text "Pokud chcete opravit překlady nebo navrhnout další jazyky, připojte se na server {a=https://discord.gg/u9GwfyjJNs}{image=gui/discord_32.png} Discord{/a}." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]

        elif renpy.game.preferences.language == "dutch":
            text "Vertalingen worden gegenereerd met behulp van kunstmatige intelligentie. Er kunnen fouten, verkeerde vertalingen of lege vertalingen zijn." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]
            text "Als je vertalingen wilt corrigeren of extra talen wilt voorstellen, meld je dan aan bij de {a=https://discord.gg/u9GwfyjJNs}{image=gui/discord_32.png} Discord{/a}-server." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]

        elif renpy.game.preferences.language == "hindi":
            text "अनुवाद कृत्रिम बुद्धिमत्ता का उपयोग करके उत्पन्न किए गए हैं। इसमें गलतियाँ, गलत अनुवाद या खाली अनुवाद हो सकते हैं।" size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]
            text "यदि आप अनुवाद सही करना चाहते हैं या अतिरिक्त भाषाओं का सुझाव देना चाहते हैं, तो कृपया डिस्कॉर्ड सर्वर में शामिल हों।" size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]

        elif renpy.game.preferences.language == "italian":
            text "Le traduzioni sono generate utilizzando l'intelligenza artificiale. Possono esserci errori, traduzioni errate o traduzioni vuote." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]
            text "Se desideri correggere le traduzioni o suggerire lingue aggiuntive, ti preghiamo di unirti al server {a=https://discord.gg/u9GwfyjJNs}{image=gui/discord_32.png} Discord{/a}." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]

        elif renpy.game.preferences.language == "korean":
            text "번역은 인공지능을 사용하여 생성됩니다. 실수, 잘못된 번역 또는 빈 번역이 있을 수 있습니다." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]
            text "번역을 수정하거나 추가 언어를 제안하려면 {a=https://discord.gg/u9GwfyjJNs}{image=gui/discord_32.png} Discord{/a} 서버에 가입해 주세요." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]

        elif renpy.game.preferences.language == "polish":
            text "Tłumaczenia są generowane przy użyciu sztucznej inteligencji. Mogą wystąpić błędy, błędne tłumaczenia lub puste tłumaczenia." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]
            text "Jeśli chcesz poprawić tłumaczenia lub zasugerować dodatkowe języki, dołącz do serwera {a=https://discord.gg/u9GwfyjJNs}{image=gui/discord_32.png} Discord{/a}." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]

        elif renpy.game.preferences.language == "thai":
            text "การแปลถูกสร้างขึ้นโดยใช้ปัญญาประดิษฐ์ อาจมีข้อผิดพลาด การแปลผิดพลาด หรือการแปลที่ว่างเปล่า" size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]
            text "หากคุณต้องการแก้ไขการแปลหรือเสนอภาษาเพิ่มเติม โปรดเข้าร่วมเซิร์ฟเวอร์ {a=https://discord.gg/u9GwfyjJNs}{image=gui/discord_32.png} Discord{/a}" size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]

        elif renpy.game.preferences.language == "vietnamese":
            text "Các bản dịch được tạo ra bằng trí tuệ nhân tạo. Có thể có lỗi, bản dịch sai hoặc bản dịch trống." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]
            text "Nếu bạn muốn sửa chữa các bản dịch hoặc đề xuất thêm ngôn ngữ, vui lòng tham gia máy chủ {a=https://discord.gg/u9GwfyjJNs}{image=gui/discord_32.png} Discord{/a}." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]

        elif renpy.game.preferences.language == "russian":
            text "Перевод был сгенерирован с помощью ИИ. Не исключено наличие ошибок, неправильно переведенных слов, ну или же вообще отсутствие перевода" size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]
            text "Если вы хотите подправить перевод или предложить перевод на свой язык, пожалуйста присоединитесь к нашему серверу в {a=https://discord.gg/u9GwfyjJNs}{image=gui/discord_32.png} Discord{/a}." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]
        elif renpy.game.preferences.language == "arabic":
            text "تم إنشاء الترجمات باستخدام الذكاء الاصطناعي. قد تحتوي على أخطاء أو ترجمات غير صحيحة أو ترجمات فارغة." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]
            text "إذا كنت ترغب في تصحيح أي ترجمات أو اقتراح لغات إضافية، يرجى الانضمام إلى الخادم {a=https://discord.gg/u9GwfyjJNs}{image=gui/discord_32.png} Discord{/a}." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]
        elif renpy.game.preferences.language == "indonesian":
            text "Terjemahan dibuat menggunakan kecerdasan buatan. Mungkin terdapat kesalahan, terjemahan yang salah, atau terjemahan kosong." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]
            text "Jika Anda ingin memperbaiki terjemahan atau menyarankan bahasa tambahan, silakan bergabung dengan server {a=https://discord.gg/u9GwfyjJNs}{image=gui/discord_32.png} Discord{/a}." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]
        elif renpy.game.preferences.language == "ukrainian":
            text "Переклади генеруються за допомогою штучного інтелекту. Можливі помилки, невірні переклади або порожні переклади." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]
            text "Якщо ви хочете виправити будь-які переклади або запропонувати додаткові мови, будь ласка, приєднуйтесь до сервера {a=https://discord.gg/u9GwfyjJNs}{image=gui/discord_32.png} Discord{/a}." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]
        else:
            text "Translations are generated using artificial intelligence. There may be mistakes, mistranslations, or empty translations." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]
            text "If you want to correct any translations or suggest additional languages, please join the {a=https://discord.gg/u9GwfyjJNs}{image=gui/discord_32.png} Discord{/a} server." size 40 color "#FFFFFF" outlines [(4, "#000000", 1, 1)]

    vbox:
        xalign 0.65
        yalign 0.80

        textbutton "Back":
            action Return()
            at choice_hover
            style "language_button"

###



style language_button:
    size 40
    color "#FFFFFF"
    xalign 0.5
    outlines [(1, "#000000", 1, 1)]
    background Frame("gui/lang_button.png", 10, 10)
    hover_background Frame("gui/lang_button_hover.png", 10, 10)

translate chinese_simplified style default:
    font "NotoSansSC-SemiBold.ttf"

translate chinese_simplified python:
    gui.text_font = "NotoSansSC-SemiBold.ttf"
    gui.name_text_font = "NotoSansSC-SemiBold.ttf"
    gui.interface_text_font = "NotoSansSC-SemiBold.ttf"
    gui.button_text_font = "NotoSansSC-SemiBold.ttf"
    gui.choice_button_text_font = "NotoSansSC-SemiBold.ttf"
    gui.system_font = "NotoSansSC-SemiBold.ttf"
    gui.main_font = "NotoSansSC-SemiBold.ttf"

translate chinese_traditional style default:
    font "NotoSansTC-SemiBold.ttf"

translate chinese_traditional python:
    gui.text_font = "NotoSansTC-SemiBold.ttf"
    gui.name_text_font = "NotoSansTC-SemiBold.ttf"
    gui.interface_text_font = "NotoSansTC-SemiBold.ttf"
    gui.button_text_font = "NotoSansTC-SemiBold.ttf"
    gui.choice_button_text_font = "NotoSansTC-SemiBold.ttf"
    gui.system_font = "NotoSansTC-SemiBold.ttf"
    gui.main_font = "NotoSansTC-SemiBold.ttf"

translate korean style default:
    font "NotoSansKR-SemiBold.ttf"

translate korean python:
    gui.text_font = "NotoSansKR-SemiBold.ttf"
    gui.name_text_font = "NotoSansKR-SemiBold.ttf"
    gui.interface_text_font = "NotoSansKR-SemiBold.ttf"
    gui.button_text_font = "NotoSansKR-SemiBold.ttf"
    gui.choice_button_text_font = "NotoSansKR-SemiBold.ttf"
    gui.system_font = "NotoSansKR-SemiBold.ttf"
    gui.main_font = "NotoSansKR-SemiBold.ttf"

translate japanese style default:
    font "NotoSansJP-SemiBold.ttf"

translate japanese python:
    gui.text_font = "NotoSansJP-SemiBold.ttf"
    gui.name_text_font = "NotoSansJP-SemiBold.ttf"
    gui.interface_text_font = "NotoSansJP-SemiBold.ttf"
    gui.button_text_font = "NotoSansJP-SemiBold.ttf"
    gui.choice_button_text_font = "NotoSansJP-SemiBold.ttf"
    gui.system_font = "NotoSansJP-SemiBold.ttf"
    gui.main_font = "NotoSansJP-SemiBold.ttf"

translate Russiann style default:
    font "NotoSans-SemiBold.ttf"

translate Russiann python:
    gui.text_font = "NotoSans-SemiBold.ttf"
    gui.name_text_font = "NotoSans-SemiBold.ttf"
    gui.interface_text_font = "NotoSans-SemiBold.ttf"
    gui.button_text_font = "NotoSans-SemiBold.ttf"
    gui.choice_button_text_font = "NotoSans-SemiBold.ttf"
    gui.system_font = "NotoSans-SemiBold.ttf"
    gui.main_font = "NotoSans-SemiBold.ttf"    


translate russian style default:
    font "NotoSans-SemiBold.ttf"

translate russian python:
    gui.text_font = "NotoSans-SemiBold.ttf"
    gui.name_text_font = "NotoSans-SemiBold.ttf"
    gui.interface_text_font = "NotoSans-SemiBold.ttf"
    gui.button_text_font = "NotoSans-SemiBold.ttf"
    gui.choice_button_text_font = "NotoSans-SemiBold.ttf"
    gui.system_font = "NotoSans-SemiBold.ttf"
    gui.main_font = "NotoSans-SemiBold.ttf"   

###

translate turkish style default:
    font "Inter-SemiBoldItalic.ttf"

translate turkish python:
    gui.text_font = "Inter-SemiBoldItalic.ttf"
    gui.name_text_font = "Inter-SemiBoldItalic.ttf"
    gui.interface_text_font = "Inter-SemiBoldItalic.ttf"
    gui.button_text_font = "Inter-SemiBoldItalic.ttf"
    gui.choice_button_text_font = "Inter-SemiBoldItalic.ttf"
    gui.system_font = "Inter-SemiBoldItalic.ttf"
    gui.main_font = "Inter-SemiBoldItalic.ttf"

translate thai style default:
    font "NotoSansThai-VariableFont.ttf"

translate thai python:
    gui.text_font = "NotoSansThai-VariableFont.ttf"
    gui.name_text_font = "NotoSansThai-VariableFont.ttf"
    gui.interface_text_font = "NotoSansThai-VariableFont.ttf"
    gui.button_text_font = "NotoSansThai-VariableFont.ttf"  
    gui.choice_button_text_font = "NotoSansThai-VariableFont.ttf"  
    gui.system_font = "NotoSansThai-VariableFont.ttf"  
    gui.main_font = "NotoSansThai-VariableFont.ttf"  

translate hindi style default:
    font "NotoSans-VariableFont.ttf"

translate hindi python:
    gui.text_font = "NotoSans-VariableFont.ttf"
    gui.name_text_font = "NotoSans-VariableFont.ttf"
    gui.interface_text_font = "NotoSans-VariableFont.ttf"
    gui.button_text_font = "NotoSans-VariableFont.ttf"
    gui.choice_button_text_font = "NotoSans-VariableFont.ttf"
    gui.system_font = "NotoSans-VariableFont.ttf"
    gui.main_font = "NotoSans-VariableFont.ttf"

translate czech style default:
    font "Inter-SemiBoldItalic.ttf"

translate czech python:
    gui.text_font = "Inter-SemiBoldItalic.ttf"
    gui.name_text_font = "Inter-SemiBoldItalic.ttf"
    gui.interface_text_font = "Inter-SemiBoldItalic.ttf"
    gui.button_text_font = "Inter-SemiBoldItalic.ttf"
    gui.choice_button_text_font = "Inter-SemiBoldItalic.ttf"
    gui.system_font = "Inter-SemiBoldItalic.ttf"
    gui.main_font = "Inter-SemiBoldItalic.ttf"

translate polish style default:
    font "Inter-SemiBoldItalic.ttf"

translate polish python:
    gui.text_font = "Inter-SemiBoldItalic.ttf"
    gui.name_text_font = "Inter-SemiBoldItalic.ttf"
    gui.interface_text_font = "Inter-SemiBoldItalic.ttf"
    gui.button_text_font = "Inter-SemiBoldItalic.ttf"
    gui.choice_button_text_font = "Inter-SemiBoldItalic.ttf"
    gui.system_font = "Inter-SemiBoldItalic.ttf"
    gui.main_font = "Inter-SemiBoldItalic.ttf"

translate vietnamese style default:
    font "Inter-SemiBoldItalic.ttf"

translate vietnamese python:
    gui.text_font = "Inter-SemiBoldItalic.ttf"
    gui.name_text_font = "Inter-SemiBoldItalic.ttf"
    gui.interface_text_font = "Inter-SemiBoldItalic.ttf"
    gui.button_text_font = "Inter-SemiBoldItalic.ttf"
    gui.choice_button_text_font = "Inter-SemiBoldItalic.ttf"
    gui.system_font = "Inter-SemiBoldItalic.ttf"
    gui.main_font = "Inter-SemiBoldItalic.ttf"

translate ukrainian style default:
    font "NotoSans-SemiBoldUK.ttf"

translate ukrainian python:
    gui.text_font = "NotoSans-SemiBoldUK.ttf"
    gui.name_text_font = "NotoSans-SemiBoldUK.ttf"
    gui.interface_text_font = "NotoSans-SemiBoldUK.ttf"
    gui.button_text_font = "NotoSans-SemiBoldUK.ttf"
    gui.choice_button_text_font = "NotoSans-SemiBoldUK.ttf"
    gui.system_font = "NotoSans-SemiBoldUK.ttf"
    gui.main_font = "NotoSans-SemiBoldUK.ttf"

translate arabic style default:
    font "IBMPlexSansArabic-SemiBold.ttf"

translate arabic python:
    gui.text_font = "IBMPlexSansArabic-SemiBold.ttf"
    gui.name_text_font = "IBMPlexSansArabic-SemiBold.ttf"
    gui.interface_text_font = "IBMPlexSansArabic-SemiBold.ttf"
    gui.button_text_font = "IBMPlexSansArabic-SemiBold.ttf"
    gui.choice_button_text_font = "IBMPlexSansArabic-SemiBold.ttf"
    gui.system_font = "IBMPlexSansArabic-SemiBold.ttf"
    gui.main_font = "IBMPlexSansArabic-SemiBold.ttf"
    gui.config.rtl = True
    gui.dialogue_width = 1500
