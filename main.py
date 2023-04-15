from flet import *
import random

def main(page:Page):
	page.theme_mode = "light"
	# NOW CREATE EaCH COntaINER
	myloopcontainer = Row(wrap=True)


	def youdrag(e):
		# CHANGE WIDTH OF delete here 
		# OPTIONAL IF YoU CAN EFFECT DRAG DELETE 
		# THIS WILL ZOOM EFFECT IF YOU DRAG TO delete here
		e.control.content.width = 300
		e.control.content.height = 300
		e.control.content.bgcolor="yellow"
		print("YOU DRAG ")
		page.update()


	def youaccept(e):
		# NOW GET SRC OF YOU CONTAInER
		src = page.get_control(e.src_id)

		e.control.content.width = 200
		e.control.content.height = 200
		e.control.content.bgcolor="red"
		# GET NUMBER OF CONTAInER
		you_value = src.content.content.value

		print("YOU ACCEPT ",you_value)
		# NOW LOOP AND FIND IF FOUND THEN REMOVE ContainER
		for b in myloopcontainer.controls:
			# IF FOUND
			if b.content.content.value == you_value:
				# THEN REMOVE
				myloopcontainer.controls.remove(b)
				# show snack bar
				page.snack_bar = SnackBar(
					Text("Success delete",size=30,color="white"),
					bgcolor="red"
					)
				page.snack_bar.open = True



		page.update()

	def youcancel(e):
		e.control.content.width = 200
		e.control.content.height = 200
		e.control.content.bgcolor="red"
		print("YOU CANCEL  ")
		page.update()


	# NOW CREATE CONTAINER COLOR 
	a = ["brown","green","orange","purple"]

	# NOW LOOP AND CREATE CONTAINER
	for x in range(0,4):
		myloopcontainer.controls.append(
			# CREATE DRAGABLE CONTAINER 
			Draggable(
				content=Container(
					width=100,
					height=100,
					bgcolor=random.choice(a),
					alignment=alignment.center,
					content=Text(x,size=30,color="white")
					)
				)
			)


	page.add(
		Column([
			myloopcontainer,
			DragTarget(
			content=Container(
				width=200,
				height=200,
				bgcolor="red",
				alignment=alignment.center,
				content=Text("delete here",size=30,color="white")
				),
			# IF YOU DRAG Container HERE
			on_will_accept=youdrag,
			# IF ACCEPT 
			on_accept=youaccept,
			# IF YOU CANCEL FOR ACCEPT DRAG
			on_leave=youcancel

				)
			])

		)

flet.app(target=main)
