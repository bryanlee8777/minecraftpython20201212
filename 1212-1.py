from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
mc.setSign(x+1,y,z,63,0,"2020/12/12","我愛minecraft","也愛Python")