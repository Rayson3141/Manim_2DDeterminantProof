from manimlib.imports import *
import numpy as np

class ParallelogramAnimation(Scene):
    def construct(self):
        #Text
        det_original = TexMobject(r"\begin{vmatrix} a & c \\ b & d \end{vmatrix}= \quad ?")
        det_transform1 = TexMobject(r"\begin{vmatrix} a & c \\ b & d \end{vmatrix} = A - B")
        det_transform2 = TexMobject(r"\begin{vmatrix} a & c \\ b & d \end{vmatrix} = \begin{vmatrix} a & c \\ 0 & d \end{vmatrix} + \begin{vmatrix} 0 & c \\ b & d \end{vmatrix}")
        det_transform3 = TexMobject(r"\begin{vmatrix} a & c \\ b & d \end{vmatrix} = ad - bc")
        det_original.scale(1.5)
        det_original.to_edge(DL, buff=1.5)
        det_ori_back = self.backrec(det_original)
        det0 = VGroup(det_ori_back,det_original)

        #Colour
        ColorM = [[[-1,None],[-3,-2]],[[-12,None],[-25,-13]],[[-2,None],[-5,-3]]]
        
        # ShowCreation a coordinate system
        grid = NumberPlane(
            x_range=(-10, 10, 1),
            y_range=(-5, 5, 1)
        )

        # ShowCreation vectors
        vector1 = Vector([3,1])
        vector2 = Vector([2,2])
        vectorf = Vector([3,1])      

        vector2_p = self.perp(vector2)
        vector1_b1 = Vector([vector1.get_end()[0],0])
        vector1_b2 = Vector([0,vector1.get_end()[1]])
        vector1b1_pr = self.projection(vector1_b1 ,vector2_p)
        vector1b2_pr = self.projection(vector1_b2 ,vector2_p)

        vector1_pr = self.projection(vector1 ,vector2_p)
        vector1b = VGroup(vector1_b1,vector1_b2)
        vector1b_pr = VGroup(vector1b1_pr,vector1b2_pr)

        #Vector Label
        vector1_l = self.vectlabel(vector1,"a","b",RIGHT)
        vector2_l = self.vectlabel(vector2,"c","d",LEFT)
        vector1_b1_l = self.vectlabel(vector1_b1,"a","0",RIGHT)
        vector1_b2_l = self.vectlabel(vector1_b2,"0","b",LEFT)
        vectorf1_l = self.vectlabel(vector1,"a","b",RIGHT)
        vectorf2_l = self.vectlabel(vector2,"c","d",LEFT)

        # ShowCreation parallelogram
        parallelogram_0 = self.parallelogram(vector1,vector2,"?")
        parallelogram_1 = self.parallelogram(vector1_pr,vector2,"?")
        parallelogram_21 = self.parallelogram(vector1b1_pr,vector2,"A")
        parallelogram_22 = self.parallelogram(vector1b2_pr,vector2,"B")
        parallelogram_2 = VGroup(parallelogram_21, parallelogram_22)
        parallelogram_31 = self.parallelogram(vector1_b1,vector2,"A")
        parallelogram_32 = self.parallelogram(vector1_b2,vector2,"B")
        parallelogram_3 = VGroup(parallelogram_31, parallelogram_32)
        parallelogram_41 = self.parallelogram(vector1_b1,vector2,"ad")
        parallelogram_42 = self.parallelogram(vector1_b2,vector2,"bc")
        parallelogram_4 = VGroup(parallelogram_41, parallelogram_42)
        parallelogram_5 = self.parallelogram(vector1,vector2,"ad-bc")

        # Dashedlines
        d0 = self.dashline(vector1,vector2)
        d1 = self.dashline(vector1_b1,vector2)
        d2 = self.dashline(vector1_b2,vector2)


        #Setup
        self.play(ShowCreation(grid), ShowCreation(vector1),ShowCreation(vector1_l), ShowCreation(vector2),ShowCreation(vector2_l),ShowCreation(det0))
        self.play(ShowCreation(parallelogram_0))
        self.wait(2)

        #Shear
        self.play(ShowCreation(d0),Uncreate(vector1_l),Uncreate(vector2_l))
        self.play(Transform(vector1,vector1_pr),Transform(parallelogram_0,parallelogram_1))
        self.play(Uncreate(d0))
        self.wait(2)

        #Split
        self.play(Transform(vector1,vector1b_pr),Transform(parallelogram_0,parallelogram_2),
                  self.detTrans(det0,det_transform1,ColorM[0]))
        self.wait(2)

        #Shear Back
        self.play(ShowCreation(d1),ShowCreation(d2))
        self.play(Transform(vector1,vector1b),Transform(parallelogram_0,parallelogram_3),ShowCreation(vector1_b1_l),ShowCreation(vector1_b2_l))
        self.play(Uncreate(d1),Uncreate(d2))
        self.wait(2)

        #Ans
        self.play(Transform(parallelogram_0,parallelogram_4),
                  self.detTrans(det0,det_transform2,ColorM[1]))
        self.wait(2)

        #End 
        self.play(Uncreate(vector1_b1_l),Uncreate(vector1_b2_l),Transform(vector1,vectorf),Transform(parallelogram_0,parallelogram_5),
                  self.detTrans(det0,det_transform3,ColorM[2]),Write(vectorf1_l),Write(vectorf2_l))
        self.wait(2)



    def parallelogram(self,vector1,vector2,text=""):
        parallelogram = Polygon(ORIGIN, vector1.get_end(), vector1.get_end() + vector2.get_end(), vector2.get_end(),
                        fill_color=BLUE, fill_opacity=0.5, color=BLUE)
        
         # Add text to the center of the parallelogram
        text_object = Text(text, font="Tex Gyre Heros")
        text_object.scale(0.8)
        text_object.move_to(parallelogram.get_center())
        
        parallelogram_with_text = VGroup(parallelogram, text_object)

        return parallelogram_with_text
 
    def projection(self,v, u):
        v = v.get_end()
        u = u.get_end()

        # Calculate the projection
        projection = np.dot(v, u) / np.linalg.norm(u)**2 * u

        return Vector(projection.tolist())
    
    def perp(self,vector1):
        vector1 = vector1.get_end()
        return Vector([-vector1[1],vector1[0]])
    
    def detTrans(self,det0,W,r):
        r1 = r[0]
        r2 = r[1]
        det_transform = W
        det_transform.scale(1.3)
        det_transform[0][r1[0]:r1[1]].set_fill(color=YELLOW)
        det_transform[0][r2[0]:r2[1]].set_fill(color=GREEN)
        det_transform.to_edge(DL, buff=1.5)
        background_rect = BackgroundRectangle(det_transform, fill_opacity=0.7, fill_color=BLACK)
        background_rect.scale(1.3)
        detT = VGroup(background_rect,det_transform)
        return Transform(det0,detT)
    
    def backrec(self,W):
        background_rect = BackgroundRectangle(W, fill_opacity=0.7, fill_color=BLACK)
        background_rect.scale(1.3)
        # background_rect.to_edge(DL, buff=1.5)
        return background_rect
    
    def dashline(self,v1,v2):
        start_point = v1.get_end()
        direction_vector = v2.get_end()*10

        # ShowCreation a dashed line
        dashed_line = DashedLine(start_point - direction_vector, start_point + direction_vector, dash_length=0.2)
        return dashed_line
    
    def vectlabel(self,v,w1,w2,x):
        label = TexMobject(r"\begin{bmatrix}"+w1+r"\\"+w2+r"\end{bmatrix}")
        label.scale(0.8)
        label.next_to(v, x)
        return label