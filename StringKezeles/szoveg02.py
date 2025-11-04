text ="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque suscipit tortor a ex interdum, id dictum augue dignissim. Donec aliquet suscipit dui eu venenatis. In euismod neque sit amet justo vulputate, imperdiet finibus neque vestibulum. Praesent massa urna, elementum sed rutrum sed, viverra id metus. In feugiat maximus lorem at efficitur. Maecenas mauris urna, auctor eu sem ac, commodo faucibus nulla. Cras scelerisque dolor sapien, quis aliquam ex varius blandit. Etiam cursus pretium augue, pulvinar scelerisque metus venenatis id. Praesent at dolor eu eros maximus tincidunt id non metus. Curabitur mollis leo in lacinia ultricies. Duis aliquam libero id lacus scelerisque ultricies."
text01 = " "
# 102

counter = 0
for i in range( len(text) ):
	
	 print( text[i], end = "" )
	 if( i % 50 == 0 and i != 0 ):
		 print()

# print( text )	
# print( "\"a\" betűk száma:", counter )
