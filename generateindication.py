class GenerateIndication:
    # init generate indication
    def init(self, giv_index):
        self.wep_index = giv_index
        self.indi2_act(self.wep_index)
        for page in range(1, 7):
            self.indi1_act(self.wep_index, page)

    def indi1_act(self, index, file_index):
        try:
            with open(f'HUD\\HudSetup\\Killtext\\HudElementsIndication{file_index}.con', 'r+') as f:
                self.write_indi(f, "kill", file_index, index)

        except FileNotFoundError as e:
            print(f"Required Indication file not exist {e}")
            return False
        finally:
            f.close()

    def indi2_act(self, index):
        try:
            with open(f'HUD\\HudSetup\\KillText\\HudElementsAttackerWeapon.con', 'r+') as f:
                self.write_indi(f, "dead", 0, index)
        except FileNotFoundError as e:
            print(f"Required AttackerWeapon file doesn't exist {e}")
        finally:
            f.close()

    def write_indi(self, file, key, indi_page, indi_index):
        kill_string = f"\nhudBuilder.createPictureNode\tIngameHud Indication{indi_page}weapon{indi_index} 270 352 216 32\nhudBuilder.setPictureNodeTexture \tIngame/Killtext/Indication/Indicationweapon{indi_index}.dds\nhudBuilder.setNodeShowVariable\tDemoRecInterfaceShow\nhudBuilder.setNodeColor\t\t1 1 1 0.8\nhudBuilder.setNodeInTime\t0.15\nhudBuilder.setNodeOutTime\t0.2\nhudBuilder.addNodeMoveShowEffect\t0 90\nhudBuilder.addNodeAlphaShowEffect\nhudBuilder.addNodeBlendEffect\t\t7 2\n\n"
        dead_string = f"\nhudBuilder.createPictureNode\tIngameHud AttackerWeapon{indi_index} 378 496 216 32\nhudBuilder.setPictureNodeTexture \tIngame/Killtext/KilledIndication/KilledIndicationWeapon{indi_index}.dds\nhudBuilder.setNodeShowVariable\tDemoRecInterfaceShow\nhudBuilder.setNodeColor\t\t1 1 1 0.8\nhudBuilder.setNodeInTime\t0.2\nhudBuilder.setNodeOutTime\t0.1\n\nhudBuilder.addNodeAlphaShowEffect\nhudBuilder.addNodeBlendEffect\t\t7 2\n"

        if key == "kill":
            file.write(kill_string)
        elif key == "dead":
            file.write(dead_string)
        else:
            print("invalid key")
        return True
