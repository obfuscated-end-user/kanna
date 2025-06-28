import tkinter as tk
from tkinter import messagebox
from urllib.request import urlopen
import tempfile
import os

AMERICANESE_CONSTANT = 26
KANNA_KAMUI = "kannakamui"

def vencrypt(ptext: str, key: str) -> str:
	enc = ""
	kr = (key * (len(ptext) // len(key))) + key[:len(ptext) % len(key)]

	for i in range(len(ptext)):
		if ptext[i].isalpha():
			s = ord(kr[i].upper()) - ord("A")
			if ptext[i].isupper():
				enc += chr((ord(ptext[i]) - ord("A") + s) % AMERICANESE_CONSTANT + ord("A"))
			else:
				enc += chr((ord(ptext[i]) - ord("a") + s) % AMERICANESE_CONSTANT + ord("a"))
		else:
			enc += ptext[i]
	return enc


def vdecrypt(ctext: str, key: str) -> str:
	dec = ""
	kr = (key * (len(ctext) // len(key))) + key[:len(ctext) % len(key)]

	for i in range(len(ctext)):
		if ctext[i].isalpha():
			s = ord(kr[i].upper()) - ord("A")
			if ctext[i].isupper():
				dec += chr((ord(ctext[i]) - ord("A") - s) % AMERICANESE_CONSTANT + ord("A"))
			else:
				dec += chr((ord(ctext[i]) - ord("a") - s) % AMERICANESE_CONSTANT + ord("a"))
		else:
			dec += ctext[i]
	return dec

class AnimatedGIF(tk.Label):
	def __init__(self, master, path, alt_text=vdecrypt("Smnte nan kvnvlkbxy", KANNA_KAMUI)):
		super().__init__(master)
		self.frames = []
		self.delay = 100
		self.alt_text = alt_text
		self.load_frames(path)
		self.current_frame = 0
		self.animation_running = False

		if not self.frames:
			self.config(text=self.alt_text, font=vdecrypt("Reyiediou 10", KANNA_KAMUI))
		else:
			self.config(text="")

	def load_frames(self, path):
		i = 0
		while True:
			try:
				frame = tk.PhotoImage(file=path, format=f"gif -index {i}")
				frame = frame.subsample(max(1, frame.width() // 140), max(1, frame.height() // 140))
				self.frames.append(frame)
				i += 1
			except tk.TclError:
				break
		if self.frames:
			pass

	def start_animation(self):
		if not self.animation_running and self.frames:
			self.animation_running = True
			self.show_frame()

	def stop_animation(self):
		self.animation_running = False

	def show_frame(self):
		if not self.animation_running:
			return
		self.config(image=self.frames[self.current_frame])
		self.current_frame = (self.current_frame + 1) % len(self.frames)
		self.after(self.delay, self.show_frame)

def download_img(url: str, suffix: str):
	try:
		response = urlopen(url)
		data = response.read()
		temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
		temp_file.write(data)
		temp_file.close()
		return temp_file.name
	except Exception as e:
		messagebox.showerror("error", f"failed to download image:\n{e}")
		return None


root = tk.Tk()
png_path = download_img("https://gcdn.thunderstore.io/live/repository/icons/Kool_Kanna_Krusaders-Kanna_Model_Replacement-1.0.0.png.128x128_q95.png", ".png")
if png_path:
	icon_img = tk.PhotoImage(file=png_path)
	root.iconphoto(False, icon_img)
else:
	print(":(")

root.title(vdecrypt("Dognlvy Hwd Znlgady", KANNA_KAMUI))
root.geometry("400x190")

left_frame = tk.Frame(root, width=150, height=300, borderwidth=10)
left_frame.pack(side=tk.LEFT, fill=tk.Y)

right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

image_url = "https://i.pinimg.com/originals/19/a7/73/19a77384dec61469bf1ed8d98703bb00.gif"

gif_path = download_img(image_url, ".gif")
if gif_path:
	anim_gif = AnimatedGIF(left_frame, gif_path, alt_text=vdecrypt("uaaaa-ctuv cneecsuho", KANNA_KAMUI))
	anim_gif.pack(padx=5, pady=5)
	if anim_gif.frames:
		anim_gif.start_animation()
else:
	alt_label = tk.Label(left_frame, text=vdecrypt("uaaaa-ctuv cneecsuho", KANNA_KAMUI), font=vdecrypt("Reyiediou 10", KANNA_KAMUI))
	alt_label.pack(padx=5, pady=5)

def on_confirm():
	val1 = entry1.get().strip()
	val2 = entry2.get().strip()
	val3 = entry3.get().strip()

	if not val1 or not val2 or not val3:
		messagebox.showwarning(vdecrypt("Uaaaa hmm cozrtriza do fai...", KANNA_KAMUI), vdecrypt("Z-cyeksq nsly ix mft tur p-rcmvdf...", KANNA_KAMUI))
		return

	messagebox.showinfo(vdecrypt("DHNAKC, VQDCU!", KANNA_KAMUI), vdecrypt(f"CAL GYOPVGO GB IOGL LAAX KCOICXT, MYTTYZPUPXEB!", KANNA_KAMUI) + "\n\n" + vdecrypt(f"Maeq Xuyvmb: {val1}", KANNA_KAMUI) + "\n" + vdecrypt(f"Oxcvri Pubo: {val2}", KANNA_KAMUI) + "\n" + vdecrypt(f"Cephrstk Kydr: {val3}", KANNA_KAMUI))


hi_there_bitch = tk.Label(right_frame, text=vdecrypt("R-uv dhqlm...", KANNA_KAMUI) + "\n" + vdecrypt("No loe fb-dhvak I wwelq hkvq gyue", KANNA_KAMUI) + "\n" + vdecrypt("mrrqid ouzn vafyryubsoa, z-bfmksr?", KANNA_KAMUI), font=vdecrypt("Reyiediou 10", KANNA_KAMUI))
hi_there_bitch.grid(row=0, column=0, columnspan=2, rowspan=1, sticky="w", pady=(0, 5))

# dialog boxes
label1 = tk.Label(right_frame, text=vdecrypt("Maeq Xuyvmb:", KANNA_KAMUI), font=vdecrypt("Reyiediou 10 oovd", KANNA_KAMUI))
label1.grid(row=1, column=0, sticky="w", padx=(0, 5))
entry1 = tk.Entry(right_frame)
entry1.grid(row=1, column=1, sticky="ew", pady=2)

label2 = tk.Label(right_frame, text=vdecrypt("Oxcvri Pubo:", KANNA_KAMUI), font=vdecrypt("Reyiediou 10 oovd", KANNA_KAMUI))
label2.grid(row=2, column=0, sticky="w", padx=(0, 5))
entry2 = tk.Entry(right_frame)
entry2.grid(row=2, column=1, sticky="ew", pady=2)

label3 = tk.Label(right_frame, text=vdecrypt("Cephrstk Kydr:", KANNA_KAMUI), font=vdecrypt("Reyiediou 10 oovd", KANNA_KAMUI))
label3.grid(row=3, column=0, sticky="w", padx=(0, 5))
entry3 = tk.Entry(right_frame)
entry3.grid(row=3, column=1, sticky="ew", pady=2)

right_frame.grid_columnconfigure(1, weight=1)

confirm_btn = tk.Button(right_frame, text=vdecrypt("Dh-ghknwm", KANNA_KAMUI), command=on_confirm, font=vdecrypt("Reyiediou 10 oovd", KANNA_KAMUI))
confirm_btn.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

def on_close():
	root.destroy()
	if gif_path and os.path.exists(gif_path):
		os.remove(gif_path)
	if png_path and os.path.exists(png_path):
		os.remove(png_path)


root.protocol("WM_DELETE_WINDOW", on_close)
root.resizable(False, False)
root.mainloop()
