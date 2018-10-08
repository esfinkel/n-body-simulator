import numpy as np
import time
import turtle
import tkinter as tk
import random

class Body:
    bodies = []
    number = 0
    Screens = []
    G = 6.6e-11
    
    def theta(_px, _py):
        return np.arctan2(_py, _px)
    
    def meters_to_pixels(meters):
        return meters/(3E7)
    
    def earth_moon(hours):
        earth = Body(5.97E24,0,0,0,0)
        moon = Body(7.35E22,3.84E8,0,0,1000)
        Body.run_draw(600,hours*3600)
    
    def printout():
        infos = ['Mass = '+str(body.mass)+'; x = '+str(body.x)+'; y = '+str(body.y)+'; vx = '+str(body.vx)+'; vy = '+str(body.vy) for body in Body.bodies]
        info = '\n'.join(infos)
        print(info)
    
    def status():
        Body.printout()
    
    def run_draw(h,duration,r=2):
        root = tk.Tk()
        canvas = turtle.ScrolledCanvas(root)
        canvas.pack(expand=True, fill='both')
        #wn = turtle.Screen()
        Body.Screens.append(root)
        turt = turtle.RawTurtle(canvas)
        turt.clear()
        turt.ht()
        turt.up()
        turt.speed(0)
        #rgb = (255,255,255)
        #turt.colormode(255)
        #turt.pencolor(.955,.955,.955)
        steps = duration // h
        for i in range(steps):
            for j in Body.bodies:
                j.update(h)
            if i%10==0:
                Body.circles(turt,r)
    
    def stop(ind):
        Body.bodies[ind].vx = 0
        Body.bodies[ind].vy = 0
            
    def circles(turt,r):
        #helper method
        for body in Body.bodies:
            turt.goto(Body.meters_to_pixels(body.x),Body.meters_to_pixels(body.y))
            turt.down()
            turt.circle(r)
            turt.up()
        
    def draw(r=2):
        root = tk.Tk()
        canvas = turtle.ScrolledCanvas(root)
        canvas.pack(expand=True, fill='both')
        #wn = turtle.Screen()
        Body.Screens.append(root)
        turt = turtle.RawTurtle(canvas)
        turt.clear()
        turt.ht()
        turt.up()
        Body.circles(turt,r)
    
    def close():
        for root in Body.Screens:
            try:
                root.destroy()
            except:
                'ok'
    
    def run(h,duration):
        # h = time step
        steps = duration // h
        for i in range(steps):
            for i in Body.bodies:
                i.update(h)
    
    def evolve(h,duration):
        run(h,duration)
   
    def update(self,h):
        Fx = 0
        Fy = 0
        for body in Body.bodies:
            if not body == self:
                dx = self.x - body.x
                dy = self.y - body.y
                dist = (dx**2 + dy**2)**0.5
                F = -Body.G*self.mass*body.mass/ (dist**2)
                Fx += F*np.cos(Body.theta(dx,dy))
                Fy += F*np.sin(Body.theta(dx,dy))
        ax = Fx / self.mass
        ay = Fy / self.mass
        o_vx = self.vx
        o_vy = self.vy
        self.vx += ax * h
        self.vy += ay * h
        self.x += (o_vx + self.vx)/2 * h
        self.y += (o_vy + self.vy)/2 * h
    
    def default():
        mass = random.uniform(6E22,8E22)
        x = random.uniform(-1E9,1E9)
        y = random.uniform(-1E9,1E9)
        vx = random.uniform(-4E3,4E3)
        vy = random.uniform(-4E3,4E3)
        Body(mass,x,y,vx,vy)
    
    def __init__(self,mass,x,y,vx,vy):
        self.mass = mass
        for body in Body.bodies:
            if abs(body.x - x)<.001 and abs(body.y - y)<.001:
                raise Exception('Already an object at that spot.')
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        Body.bodies.append(self)
        Body.number += 1

if __name__ == '__main__':
    Body.earth_moon(30)
    time.sleep(6)
    #Body.Screens[0].exitonclick() 