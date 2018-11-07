init 2 python:

    ######## Do NOT edit anything above this line. ########

    # Input your language label by replacing all of the your_label_here. Do NOT remove the pair of ''.
    # You can check what your language label is in your map.txt file (first line).

    # Example:
        # if language.get_label() == 'thai':
            # your_label = 'thai'

    if language.get_label() == 'polish':
        your_label = 'polish'

        # Replace these strings (texts between pairs of "") with your translation of those strings.

        # Example:
            # TranslateCWT01 = "โปรดกรุณาอ่าน"

        TranslateCWT01 = "Uwaga"
        TranslateCWT02 = "Nekojishi zostało zaktualizowane do wersji "
        TranslateCWT03 = "Poprzednio zapisane gry mogą nie być kompatybilne. Zaleca się ich usunięcie aby uniknąć wystąpienia błędów."
        TranslateCWT04 = "Proszę zdecyduj, czy chcesz zachować swoje pliki zapisu."
        TranslateCWT05 = "Uwaga 1: Jeśli usuniesz te pliki, mogą one zostać przywrócone w razie potrzeby z następującego folderu:"
        TranslateCWT06 = "Uwaga 2: Odblokowane elementy galerii, wpisy w glosariuszu oraz uzyskane zakończenia zostaną zachowane."
        TranslateCWT07 = "ZACHOWAJ TE PLIKI"
        TranslateCWT08 = "USUŃ PLIKI ZAPISU"

    ######## Do NOT edit anything below this line. ########

init 2:
    if language.get_label() == your_label:
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
                        if language.get_label() == your_label:
                            text "[TranslateCWT01]" color title_color xalign 0.5 size title_text_size
                            text "Attention" color title_color xalign 0.5 size title_text_size
                            text ""
                            text "[TranslateCWT02] [config.version]" size content_text_size
                            text "[TranslateCWT03]" size content_text_size
                            text "[TranslateCWT04]" size content_text_size
                            text "[TranslateCWT05] [save_dir]" size content_text_size
                            text "[TranslateCWT06]" size content_text_size
                        else:
                            text "[[　注意　]" color title_color xalign 0.5 size title_text_size font bold_font
                            text "Attention" color title_color xalign 0.5 size title_text_size font bold_font
                            text ""
                            text ("家有大貓已更新為%s，有可能會有存檔不相容的問題，可刪除存檔以避免讀檔時出現錯誤。" % config.version) size content_text_size
                            text "請選擇保留存檔或刪除存檔。" size content_text_size
                            text ("註一：刪除的存檔會保留在(%s)資料夾中，玩家可以手動復原。" % save_dir) size content_text_size
                            text "註二：刪除存檔依然會保留已開啟的註釋、結局、圖片。" size content_text_size
                        text ""
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
                                    if language.get_label() == your_label:
                                        text "[TranslateCWT07]" size button_text_Size xalign 0.5
                                    else:
                                        text "保留存檔" size button_text_Size xalign 0.5
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
                                    if language.get_label() == your_label:
                                        text "[TranslateCWT08]" size button_text_Size xalign 0.5
                                    else:
                                        text "刪除存檔" size button_text_Size xalign 0.5
                                    text "DELETE SAVE FILES" size button_text_Size xalign 0.5

