##############################################################################
# compatibleWarning
#
# Renpy一直存在相容性問題。只要進行大幅重構，讀檔時就有很大機率會失敗，無論有無重構到該存檔附近的程式碼。
# 故此畫面每次更新改版時皆會出現，警告使用者有相容性問題，提示可以砍掉過往存檔。

screen compatibleWarning(isClick):
    python:
        title_text_size = 30
        content_text_size = 20
        bold_font = "tl/None/NotoSansCJKtc-Bold.otf"
        button_xysize = (217, 76)
        button_text_Size = 22
        import os
        save_dir = os.path.join(config.savedir, "backup")

    window:
        style "gm_root"
        style_group "empty"
        background "#000000"

        frame:
            align (0.5,0.5)
            xmargin 180
            vbox:
                text "{font=tl/thai/CSChatThaiUI.ttf}โปรดอ่าน{/font}" color title_color xalign 0.5 size title_text_size font bold_font
                text "Attention" color title_color xalign 0.5 size title_text_size font bold_font

                text ""

                # 中文說明
                text ("Nekojishi หรือ บ้านนี้มีแมวใหญ่ ได้ทำการอัปเดตเป็นเวอร์ชัน %s แล้ว บันทึกเกมเก่าอาจจะไม่สามารถใช้ร่วมกันกับเวอร์ชันนี้ได้ เราแนะนำให้คุณลบบันทึกเก่า เพื่อป้องกันการทำงานผิดพลาดของโปรแกรม" % config.version) size content_text_size
                text "กรุณาเลือกว่าจะเก็บ หรือลบบันทึกเก่าของคุณ หลังจากนั้น กรุณาดาวน์โหลดส่วนเสริมภาษาไทยเวอร์ชันปัจจุบันที่ http://nekojishith.tumblr.com ในกรณีที่พบปัญหาความไม่เข้ากันของรุ่นเวอร์ชัน" size content_text_size
                text ("หมายเหตุ ๑: หากคุณเลือกที่จะลบ ตัวบันทึกจะถูกย้ายไปเก็บไว้ที่ (%s) และคุณสามารถกู้คืนได้ภายหลังด้วยตัวเอง" % save_dir) size content_text_size
                text "หมายเหตุ ๒: บันทึกถาวร อาทิเช่น ภาพในคลังที่เปิดแล้ว คำศัพท์ที่พบแล้ว และฉากจบที่ได้แล้ว จะไม่ถูกลบ" size content_text_size

                text ""

                # 英文說明
                text ("Nekojishi has been updated to v%s. Existing save files may no longer be compatible. It is advised to delete your save files to prevent errors." % config.version) size content_text_size
                text "Please decide to either keep or delete your save files." size content_text_size
                text ("Note 1: If deleted, files will be archived in (%s). You may restore them manually if needed." % save_dir) size content_text_size
                text "Note 2: Persistent data (gallery unlocks, glossary entries, and attained endings) will not be affected." size content_text_size

                text ""

                hbox:
                    xalign 0.5
                    spacing 150

                    default yes_hover = False

                    button:
                        xysize button_xysize
                        if isClick:
                            action [Function(compatibility.upgrade_version, remove_save_files=False), Return()]
                        hovered SetScreenVariable("yes_hover", True)
                        unhovered SetScreenVariable("yes_hover", False)
                        if yes_hover:
                            background Frame("ui/r18_button_hovered.png", left=5, top=5, tile=True)
                        else:
                            background Frame("ui/r18_button_unhovered.png", left=5, top=5, tile=True)
                        vbox:
                            align (0.5,0.5)
                            text "เก็บบันทึกเก่าไว้" size button_text_Size xalign 0.5
                            text "KEEP SAVE FILES" size button_text_Size xalign 0.5

                    default no_hover = False
                    button:
                        xysize button_xysize
                        if isClick:
                            action [Function(compatibility.upgrade_version, remove_save_files=True), Return()]
                        hovered SetScreenVariable("no_hover", True)
                        unhovered SetScreenVariable("no_hover", False)
                        if no_hover:
                            background Frame("ui/r18_button_hovered.png", left=5, top=5, tile=True)
                        else:
                            background Frame("ui/r18_button_unhovered.png", left=5, top=5, tile=True)
                        vbox:
                            align (0.5,0.5)
                            text "ลบบันทึกเก่า" size button_text_Size xalign 0.5
                            text "DELETE SAVE FILES" size button_text_Size xalign 0.5
