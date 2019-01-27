import matplotlib.pyplot as plt

fig = plt.figure()
plt.axis([0, 10, 0, 10])
t = ("Tekst możemy rozmieszczać w oknie wykresu na "
     "różne sosoby stosując polecenie plt.text np.4,1 "
     "t, ha='left', rotation=15, wrap=True")
plt.text(4, 1, t, ha='left', rotation=20, wrap=True)
plt.text(6, 5, t, ha='left', rotation=25, wrap=True)
plt.text(5, 5, t, ha='right', rotation=-25, wrap=True)
plt.text(5, 10, t, fontsize=21, style='oblique', ha='center',
         va='top', wrap=True)
plt.text(3, 4, t, family='serif', style='italic', ha='right', wrap=True)
plt.text(-1, 0, t, ha='left', rotation=-15, wrap=True)

plt.show()
