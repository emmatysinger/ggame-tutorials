from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

class SpaceGame(App):
    def __init__(self):
        super().__init__()
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(self.width, self.height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        SpaceShip((100,100))
        SpaceShip((150,150))
        SpaceShip((200,50))
    
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()

class SpaceShip(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,65,125), 4, 'vertical')

    def __init__(self,position):
        super().__init__(SpaceShip.asset,position)
        self.vx=1
        self.vy=1
        self.vr=0.01
        self.thrust=0
        self.thrustframe=1
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown","left arrow",self.leftRotate)
        SpaceGame.listenKeyEvent("keydown","right arrow",self.rightRotate)
        SpaceGame.listenKeyEvent("keydown","A",self.left)
        SpaceGame.listenKeyEvent("keydown","D",self.right)
        SpaceGame.listenKeyEvent("keydown","W",self.up)
        SpaceGame.listenKeyEvent("keydown","S",self.down)
        self.fxcenter = self.fycenter = 0.5
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)
            
    def thrustOn(self, event):
        self.thrust = 1
        
    def thrustOff(self, event):
        self.thrust = 0
    
    def rightRotate(self,event):
        self.vr -=0.01
    
    def leftRotate(self,event):
        self.vr +=0.01    
        
    def left(self,event):
        self.vx -=0.5
    def right(self,event):
        self.vx +=0.5
    def up(self,event):
        self.vy -=0.5
    def down(self,event):
        self.vy +=0.5

myapp = SpaceGame()
myapp.run()
