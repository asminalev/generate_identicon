
# Identicon

Identicon is a python3 script which generates Github like identicons.

# Usage

Generates an identicon image by passing a "text" parameter:

Output:

output/"text.png" width="250" height="250"

Help information:

To generate an identicon avatar form text parameter, run function 'image_to_file()' and the image will be written to output folder by its name and .png extension.
To run the function, create a class object and call the function with parameter:

Identicon.image_to_file('text')
***

On the other hand, there is a flask application that takes a parameter and passes to an arbitrary function that is shown
to run. 
run:
python3 app.py


