from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class Paddle(Widget):
    score = NumericProperty(0)
    def bounce_ball(self, ball):
    	if self.collide_widget(ball):
    		ball.velocity_x *= -1.2
    		
    pass

class Ball(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
    pass
    
class Game(Widget):
    ball = ObjectProperty(None)
    player_1 = ObjectProperty(None)
    player_2 = ObjectProperty(None)
	
    def serve_ball(self):
        self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))
    def on_touch_move(self, touch):
    	if touch.x < self.width / 1/4:
    		self.player_1.center_y = touch.y
    	if touch.x > self.width * 3/4:
    		self.player_2.center_y = touch.y
    	
    def update(self, dt):
        self.ball.move()
        self.player_1.bounce_ball(self.ball)
        self.player_2.bounce_ball(self.ball)
        
        if self.ball.y < 0 or self.ball.y > self.height - 50:
        	self.ball.velocity_y *= -1
        	
        if self.ball.x < 0:
        	self.ball.velocity_x *= -1
        	self.player_1.score += 1
        if self.ball.x > self.width - 50:
            self.ball.velocity_x *= -1
            self.player_2.score += 1
		
class App(App):
    def build(self):
        game = Game()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game
        
App().run()