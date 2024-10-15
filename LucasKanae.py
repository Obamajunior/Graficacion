import numpy as np 
import cv2 as cv

cap = cv.VideoCapture(0)

lkparm = dict(winSize=(15,15), maxLevel=2,
              criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

_, vframe = cap.read()
vgris = cv.cvtColor(vframe, cv.COLOR_BGR2GRAY)

p0 = np.array([(100,100), (200,100), (300,100), (400,100), (500,100), (600,100),
               (100,200), (200,200), (300,200), (400,200), (500,200), (600,200),
               (100,300), (200,300), (300,300), (400,300), (500,300), (600,300),
               (100,400), (200,400), (300,400), (400,400), (500,400), (600,400),
               (100,500), (200,500), (300,500), (400,500), (500,500), (600,500),
               (100,600), (200,600), (300,600), (400,600), (500,600), (600,600)])

p0 = np.float32(p0[:, np.newaxis, :])

mask = np.zeros_like(vframe)

while True:
    _, frame = cap.read()
    fgris = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    p1, st, err = cv.calcOpticalFlowPyrLK(vgris, fgris, p0, None, **lkparm)

    if p1 is None:
        vgris = cv.cvtColor(vframe, cv.COLOR_BGR2GRAY)
        p0 = np.array([(100,100), (200,100), (300,100), (400,100)])
        p0 = np.float32(p0[:, np.newaxis, :])
        mask = np.zeros_like(vframe)
        cv.imshow('ventana', frame)
    else:
        bp1 = p1[st == 1]
        bp0 = p0[st == 1]

        num_rows = 6  
        num_cols = 6  
        num_valid_points = len(bp1) 

        for row in range(num_rows):
            for col in range(num_cols):
                idx = row * num_cols + col  

                if idx >= num_valid_points:
                    continue

                # Esto conecta con el punto a la derecha
                if col < num_cols - 1 and (idx + 1) < num_valid_points:
                    nv1 = bp1[idx].ravel()
                    nv2 = bp1[idx + 1].ravel()
                    x1, y1 = int(nv1[0]), int(nv1[1])
                    x2, y2 = int(nv2[0]), int(nv2[1])
                    frame = cv.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)

                # y este conecta con el punto de abajo
                if row < num_rows - 1 and (idx + num_cols) < num_valid_points:
                    nv1 = bp1[idx].ravel()
                    nv2 = bp1[idx + num_cols].ravel()
                    x1, y1 = int(nv1[0]), int(nv1[1])
                    x2, y2 = int(nv2[0]), int(nv2[1])
                    frame = cv.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)

        for i, (nv, vj) in enumerate(zip(bp1, bp0)):
            a, b = (int(x) for x in nv.ravel())
            c, d = (int(x) for x in vj.ravel())

            frame = cv.line(frame, (c,d), (a,b), (0,0,255), 2)  
            frame = cv.circle(frame, (c,d), 2, (255,0,0), -1)  
            frame = cv.circle(frame, (a,b), 3, (0,255,0), -1)  

        cv.imshow('ventana', frame)

        vgris = fgris.copy()

        if(cv.waitKey(1) & 0xff) == 27:  
            break

cap.release()
cv.destroyAllWindows()
