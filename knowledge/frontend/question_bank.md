Do all HTML tags come in pair?
No, not all HTMLS tags come in pair. For e.g. <img>, <br>
What are some of the common lists that can be used when designing a page?
Some of the common lists that can be used are:

a) Ordered list
b) Unordered list
c) Definition list
d) Menu list
e) Directory list
What is the advantage of collapsing white space?
- The browser collapses the multiple white spaces into a single white space in HTML.
- This allows the developers to arrange the HTML code in a well organized and legible format.
Is it possible to list elements straight in an html file?
- Yes, it is possible with the use of indents.
Does a hyperlink apply only to text?
- No. The hyperlinks can be applied to both text as well as the images.
- It means that even the images can become clickable links with a capability to take the visitor to the next page.
- This can be done simply by using <a href> tag.
What hierarchy is being followed when in style sheets?
- Inline style takes priority over embedded style sheets.
- Embedded style take priority over external style sheets.
- If a single selector includes three different style definitions, the definition that is closest to the actual tag gets the priority.
What happens if the list-style-type property is used on a non-list element like a paragraph?
- Here the property will be ignored without having any effect on the paragraph.
What is the advantage of using frames?
- Frames make it easier to navigate through a site.
- The links that appear in the frame can appear through out the site.
How can I hide my source?
- No. you can’t hide your source as it is required by the browser to display your document.
How will you align a table to the right or left?
- To align the table to the right, you can use <TABLE ALIGN="right">
- To align the table to the left, you can use <TABLE ALIGN="left">
Why doesn't <TABLE WIDTH="100%"> use the full browser width?
- This is because the graphical browser is designed to leave a margin between the display area and actual content.
- The navigator also leaves some space for the scroll bar on the right side of the display area. Though, if the page is not long enough, the scroll bar doesn’t appear.
How would you automatically transfer your visitors to a new web page?
- You can do it with the help of meta tag mentioned below:
<META HTTP-EQUIV="Refresh" CONTENT="2"; URL="http://www.yourname.com">

- Place this tag between <HEAD></HEAD> .
- It will load yousite.com in 2 seconds.
You want only a vertical scrollbar and no horizontal scrollbar on your page. How would you do it?
- This can be done by defining the frame with SCROLLING = auto and having content to just fit into this frame.
- SCROLLING="yes" gets the scroll bar on both the sides, even when not needed.
- SCROLLING="no" doesn’t get the scrollbars at all, even when they are needed.
How do you refer to the .css file in the web page?
- .css file in the web page can be referred with the use of <link> tag.
- It should be kept between <head></head> tag.
Example
<link href="/css/mystyle.css" type="text/css" rel="stylesheet" />
What is a better way to design the layout of a web page – a table tag or div?
- The better way to design the layout of the webpage is by using the <div> tag.
- The <table> tag is used to present the data in tabular format.
What is a <dl> tag in HTML?
- <dl> is a definition list tag used in HTML.
- It is used with <dt> and <dd>.
- <dt> list the item while <dd> describes it.
What are empty HTML elements?
- HTML elements with no content are called empty elements.
- For eg: <br>
How to create nest tables within tables in HTML?
We can create nest table i.e. table inside a table.

To create table we use following attributes:
<table>……</table>: declare starting and ending of table.
<tr>…</tr>: declare table row.
<td>…</td>: table data.

<table>
       <tr>
             <td>first cell of the outer table</td>
             <td>second cell of the outer table, creating second table inside the first table
                           <table>
                                  <tr>
                                           <td>first cell of the second table</td>
                                           <td>second cell of the second table</td>
                                  </tr>
                           </table>
             </td>
       </tr>
</table>
Explain Non Breaking space in HTML.
When we add many spaces in the content then HTML remove all space except one space this is Non Breaking Space. To overcome this problem we use '& nbsp;'(without space between & and nbsp;). Suppose we want to add 3 space between two words then we have to use & nbsp; three time.

Example:
actual code:- hello I m Rohit Srivastava.
Display as:- Hello I m Rohit Srivastava.
But when we use & nbsp:
Actual code:- Hello & nbsp; & nbsp ; & nbsp; I m Rohit Srivastava.
Display as:- Hello I m Rohit Srivastava
NOTE: (without space between & and nbsp;)
How do I link to a location in the middle of an HTML document?
We can link to a location in the middle of an HTML document. Using Following steps:

1. Label the destination of the link : There are two ways of labeling destination using Anchor:
- NAME attribute:

Example:
<h2><a name="destination">Destination: Explanation</a></h2>

- ID attribute:

Example:
<h2 id="Destination_ID"> Destination: Explanation </h2>

2. Link to the labeled destination : We can link with the destination in the same URL page and with Different URL page.

Example:
Same URL: <a href="#Destination"> Visit to destination</a> or
Different URL: <a href="thesis.html#section2">go to Section 2 of my thesis</a>
Explain Cell Padding and Cell Spacing.
- Cell Padding : It refers to the gap or space between the cell content and cell border or cell wall.
- Cell Spacing : It refers to the gap between the two cells of same tables.

In HTML cell spacing and padding both are used with Table Border layout.

Example:
<table border cellpadding=2>
<table border cellspacing=2>
<table border cellpadding=2 cellspacing=2>
How to create a button which acts like a link?
To create buttons which act as a hyperlink, there are two ways:
<FORM ACTION="[url]" METHOD=get>
<INPUT TYPE=submit VALUE="Text on button">
</FORM>

<INPUT TYPE="submit" VALUE="Go to my link location"
ONCLICK=" http://www.careerride.com/;" />

What is difference between HTML and XHTML?
The differences between HTML and XHTML are:

1. HTML is application of Standard Generalized Markup Language(SGML) whereas XML is application of Extensible Markup Language(XML).
2. HTML is a static Web Page whereas XHTML is dynamic Web Page.
3. HTML allows programmer to perform changes in the tags and use attribute minimization whereas XHTML when user need a new markup tag then user can define it in this.
4. HTML is about displaying information whereas XHTML is about describing the information.
How many types CSS can be include in HTML?
There are three ways to include the CSS with HTML:

1. Inline CSS : It is used when only small context is to be styled.
- To use inline styles add the style attribute in the relevant tag.
2. External Style Sheet : Is used when the style is applied to many pages.
- Each page must link to the style sheet using the <link> tag. The <link> tag goes inside the head section:
<head>
<link rel="stylesheet" type="text/css" href="mystyle.css" />
</head>

3. Internal Style Sheet : Is used when a single document has a unique style.
- Internal styles sheet needs to put in the head section of an HTML page, by using the <style> tag, like this:
<head>
<style type="text/css">
hr {color:sienna}
p {margin-left:20px}
body {background-image:url("images/back40.gif")}
</style>
</head>
What are logical and physical tags in HTML?
- Logical tags are used to tell the meaning of the enclosed text. The example of the logical tag is <strong> </strong> tag. When we enclosed text in strong tag then it tell the browser that enclosed text is more important than other text.

- Physical text are used to tell the browser that how to display the text enclosed in the physical tag.
Some example of the physical tags are: <b>, <big>, <i>
Does HTML support Javascripts?
Yes, HTML supports JavaScripts. We can use JavaScript anywhere in the HTML Coding. Mainly there are four sections where we can add JavaScript in HTML.

1. Head Section : We can add JavaScript in Head section of HTML.
<head>…..Javascript…. </head>
2. Body Section : <body>….. Javascript…</body>
3. Head and Body both : We can add Javascript in both head and body section.
<body….Javascript…</body> and <head>…..Javascript…. </head>
4. External File : Script in and external file and then include in <head> ….. </head> section.
Explain marquee tag.
Marquee tag : Marquee tag is used when we want that some text or content move in the web page whether horizontally or vertically.

Syntax of Marquee tag:
<marquee>move text</marquee>

Attribute of Marquee tag are: bgcolor, direction, height, width, vspace etc.
How do I add midi music to my web page?
We can add midi Music in our HTML web page using following tag:
<bgsound src="music.mid" loop="1">

Attribute LOOP = 1 : Shows that music.mid is played only for one time. We can also set the value of loop to infinite. This tag is supported by Netscape and Internet Explorer.

Example:
<embed src="canyon.mid" Autostart=TRUE Width=145 Height=60 Loop=true>
What are new Media Elements in HTML5?
Following are the New Media Elements are present in HTML5:

1. <audio> tag : For playing audio.
2. <video> tag : For playing video.
3. <source> tag : For media resources for media elements.
4. <embed> tag : For embedded content.
5. <track> tag : For text tracks used in media players.
Explain various HTML list tags.
In HTML we can list the element in two ways:

1. Ordered list : In this list item are marked with numbers.
Syntax:
<ol>
<li> first item </li>
<li>second item </li></ol>

Display as:
1. First item
2. Second item.

2. Unordered Lists : In this item are marked with bullets.
Syntax:
<ul>
<li> first item</li>
<li>second item </li></ul>

Display as:
- First item
- Second item.
Explain HTML background.
There are two types of background in HTML:

1. Colored Background : In this the background of the html is colored.
The Syntax is:
<body bgcolor = “red”>

The value of the bgcolor can be set in three ways by hexadecimal number, an RGB value and Color name.

Example:
<body bgcolor = “black”>
<body bgcolor = “rgb(0,0,0)”>
<body bgcolor = “#000000”>

2. Image Background : In this we set the background of the website by an image. Syntax used for this is :
<body background=”study.gif”>
What is CSS?
CSS stands for Cascading Style Sheets. By using CSS with HTML we can change the look of the web page by changing the font size and color of the font. CSS plays an important role in building the website. Well written CSS file can be used to change the presentation of each web page. By including only one CSS file. It gives web site developer and user more control over the web pages.
What is difference between HTML and HTML5?
The differences between HTML and HTML5 are:

1. Document of HTML is very large as compare to the HTML5.
2. Audio and Video tags are not present in HTML whereas HTML5 contains audio and video tags.
3. Vector technology is not integral part of HTML whereas HTML5 Vector technology is the integral part of it.
4. HTML supported by all old browsers whereas HTML5 is supported by new browser.
5. In HTML web sockets are not available whereas in HTML5 Full duplex communication channel is present.

How to insert Javascript in HTML?
We can insert JavaScript in HTML using <Script tag>. JavaScript can be enclosed in <script type = text/javascript> and ending with </script>.

Example:
<html>
  <body>
        <script type="text/javascript">
               ...JavaScript….
        </script>
  </body>
</html>
What is the Use of SPAN in HTML and give one example?
SPAN : Used for the following things:

1. Highlight the any color text
2. For adding colored text
3. For adding background image to text.

Example:
<p>
<span style="color:#000000;">
In this page we use span.
</span>
</p>
What are the different way in which website layout can be made?
Website layout describes how the webpage of the website will look. It describes the content that has to be placed in columns i.e. it can be either one or many columns. There are two ways in which different layout can be created and these are called as using table method or using div method.

There are basically two tags that are used <table> and <div>.
<table> : Using this is the simplest way to create a layout.

The example code is given as:
<html>
<body>
<table width="500" border="0">
<tr>
<td colspan="2" style="background-color:#FFA500;">
<h1>Main Title</h1>
</td>
</tr>
<tr>
<td colspan="2" style="background-color:#FFA500;text-align:center;">
This is my page</td>
</tr>
</table>
</body>
</html>

<div> : It is used as a block element and is defined to group HTML elements together in one. The <div> tag is used to create multiple layouts.

The sample code is given as:
<html>
<body>
<div id="container" style="width:500px">
<h1 style="margin-bottom:0;">Main Title of Web Page</h1></div>
<b>Menu</b><br />
</div>
</body>
</html>
What is the importance of Doctype in HTML?
Doctype tag is not a HTML tag, it is just an instruction that is passed to the web browser to check for the information that is being provided by the markup language in which the page is written. Doctype is sometimes referred as Document type definition (DTD) that describes some rules that has to be followed while writing the markup language so to make the web browser understand the language and the content correctly. Doctype is very important to be placed in the beginning of the HTML and before the <HTML> tag to allow easy rendering of the pages that are used.
Differentiate different types of Doctypes from one another
Doctype helps the web browser to correctly render the web pages. There are different types of Doctype that are available and they are as follows:

1. Strict Doctype : It consists of all the HTML elements and it is also known as DTD (Document type definition) but it doesn't include the presentational and deprecated elements i.e. font, center, etc. Framesets related elements are also not allowed in this.
For example:
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">

2. Transitional Doctype : It consists of all the HTML elements and attributes. It is also known as DTD (Document type definition). It includes the presentational and deprecated elements i.e. font, center, etc. Framesets related elements are also not allowed in this.
For example:
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">

3. Frameset Doctype : It consists of all the HTML elements and attributes. It is also known as DTD (Document type definition). It includes the presentational and deprecated elements i.e. font, center, etc. Framesets related elements are also allowed in this.
For example:
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN" "http://www.w3.org/TR/html4/frameset.dtd">
Why it is important to set the meta information?
Metadata is the data about the data or the information about the data. There is a tag <meta> that is being provided for the HTML document. This information won't be displayed anywhere and will not be visible to the user. It will be parsable by the machine which will parse it according to the requirement. It consists of the elements that are related to the page description, keywords, document related element. The tag that is being used resides in the <head> section in HTML. The meta information is being used by the web browser or by the search engines to rank and let the user find the pages easily.
The meta information is being written as:
<meta name="description" content="Here you will get everything" />
What are the different types of entities in HTML?
The different types of entities that are present in HTML are < (less than) or > (greater then). It allows the special or the reserved characters are matched with the source code and then it is saved.
The sample code is being given by:
&entity_name;
OR
&#entity_number;

There is always a concept associated with it that will create more simpler provision to avoid the spaces that are being coming in between the characters or the text.
What does the elements mean in syntax given for URL in HTML?
URL stands for Uniform Resource locater. This helps just like the Internet pooling concept where the people recognize themselves and others people connected together with each other. URL allows a document to be located on World Wide Web (www).
The example of the URL is as follows with the complete element:
scheme://host.domain:port/path/filename

This code has got with no meaning but there are some elements that are defined:

scheme - Is the type of internet service. In this HTTP can be used which has to most common type.
Host – It is used to control the host name and fetch the information from other templates as well.
Domain – It defines the internet domain that is google.com.
:port – It defines the port number on the Host where the default port that is being used is 80.
path – This defines the path of the server that consists of a hierarchical directory structure.
filename - It defines the unique name for the file or the document that saves it.
How to add helper plug-ins on the webpage using HTML?
A helper application is a program that is used in the browser to help the users with lots of information that is not being provided with the applications. These helper application is known as Plug-ins. Helper application includes audio, video, etc. The tag that is used to embed is <object>. Helper application allows easy incorporation of audio and video that is controlled by the user. Helper application allow the control over the volume setting and other functions like play, stop,etc.
<object width="420" height="360" classid="clsid:02BF25D5-8C17-4B23-BC80-D3488ABDDC6B" codebase="http://www.career.com/qtplugin.cab">
<param name="src" value="hello.wav"/>
<param name="controller" value="true"/>
</object>
What is the purpose of canvas in HTML?
Canvas is an element that is used for the graphics for the web page. It uses JavaScript to bring the graphics functionality live. It allows easy way to draw the graphics and use different types of tools to create drawing on the web page. Canvas is just a rectangular area that controls the pixel of every element that is used in the web page. Canvas uses methods like paths, circles, etc.
The canvas element will be used as follows:
<canvas id="can" width="200" height="100"></canvas>

The canvas element includes id, width and height settings and with the javascript it gets used like:
<script type="text/javascript">
var c=document.getElementById("can");
var ctx=c.getContext("2d");
ctx.fillStyle="#FF0000";
ctx.fillRect(0,0,150,75);
</script>
What is the purpose of iframe in HTML?
Iframe is called as inline frame that places one HTML document in a frame. It is different from the object element as the inline frame can be made in the target frame. The target frame consists of the links that is defined by other elements used in the web page. Iframe is used to focus on printing or viewing of the source. Iframe can be used by the user in those browser that supports it. If they have used iframe also then the incompatible browser won't display the actual but display of the alternative text will take place. The content of the iframe is being written in between <iframe>.........</iframe>.
The sample example is given below:
<iframe src="http://www.abc.com"></iframe>
What are the different types of frames tags used in HTML?
Frames allow the display of the document visually. It allows the window to be split into segments that can contain multiple different documents. It can utilize many resources and repeat some parts of the layout that can be used in a frame.

Frames consists of different types of tags and they are as follows:

1. <frameset>...</frameset> : It consists of the frames that includes the layout using the attributes of rows and cols.
2. <frame> or <frame/> : It consists of a single frame and gets included within the frameset. It is always come up with a src attribute that provides the source that has to be shown in a particular frame.
3. <noframes>...</noframes> : It consists of the normal HTML content that is used to show no frames.
4. <iframe>...</iframe> : It consists of internal frame that will contain the src attribute to include the frame that is internal to a particular region.
Write a code to change the color of the background or text? Explain the elements involved in it.
To change the color of the background of the body or the text there is a <body> tag that has to be included where there are some elements that has to be used to set the properties of it.
The code is as follows:
<html>
<head>
</head>
<BODY BGCOLOR="#ffffff" TEXT="#000000" LINK="#000000" VLINK="#000000" ALINK="#ffff00">
</body>
</html>

The elements that are used in this tag is as follows:

1. BGCOLOR : Represents the background color which will be applied totally on the body if there is no other bgcolor used with any other tag internally.
2. TEXT : Represents the color of the text that will be applied to the complete text present in the body.
3. LINK : Represents the color of all the text links that are present inside the body.
4. VLINK : Represents the color of the links that has already been visited.
5. ALINK : Represents the color of the text links that will change when the page accessed will be active.
What is the main function of <pre> tag in HTML?
<pre> tag defines the pre-formatted text that is used to display the text with the fixed width and uses a predefined fonts and it keeps both spaces and line breaks separate and show the text as it is.
The code that can be used to display the text that can be written in whatever way the user wants is as follows:
<pre>
Text in a pre element ----//
is displayed in a fixed-width
font, and it preserves
both spaces and
line breaks
</pre>
How can tables be made nested in HTML?
Tables can be made nested by making it come in another table. This consists of many attributes and tags that can be used in nesting the tables.

The tags that are used for the table is as follows:

<TR> : This is the tag that has to be written after the <table> tag and before any other tags. This makes a table row that store the data elements.
<TD> : This tag can be used anywhere and it consists of the data that has to come on the website.
<TH> : This tag consists of the table heading.

The sample code will explain the above explanation much better:
<table>
<tr>
<td>this is the first cell</td>
<td>this is the second cell
<table> <!--Starting of the table that is embedded inside another table-->
<tr>
<td>this is the first cell second table</td>
<td>this is the second cell of second table</td>
</tr>
</table>
</td>
</tr>
</table>
How can tables be used inside a form? Explain with an example.
A form can consist of the table and its properties to display it on the web page. The form is placed with the <td> tag that includes the data of the table. This can also be used to position the form in relation to the other content. The table will be added within the form.

The code is given as:
<FORM ACTION="[URL]">
<TABLE>
<TR>
<TH>This is the table heading</TH>
<TD><INPUT TYPE="text" NAME="account"></TD>
</TR>
<TR>
<TH>This is another heading for a button</TH>
<TD><INPUT TYPE="password" NAME="password"></TD>
</TR>
<TR>
<TD> </TD>
<TD><INPUT TYPE="submit" NAME="Log On"></TD>
</TR>
</TABLE>
</FORM>

In this the form elements are getting used inside the table tags like <input type>, <text area>, etc. The form input will be given using the <td> tag that displays the table data and related information accordingly.
What are the different ways to use different colors for different links or same link?
The presentation is being done by CSS that is used with the HTML, to give the style to the HTML content. This is called as style sheet. The links can be specified in different colors by the following way:
a:link {color: blue; background: white}
a:visited {color: purple; background: white}
a:active {color: red; background: white}

This is the CSS properties that is being defined to set the color for the links that are active, visited and normal link. User can use the class attribute in the tags like <a> to use it and see the change in the link color. It is shown as:
<a class="exp" href="[URL]">example of the link</a>

The style sheet can be modified according to the code that is being written. The coding will include:
a.exp:link {color: yellow; background: black}
a.exp:visited {color: white; background: black}
a.exp:active {color: red; background: black}
How to upload files using HTML to website?
The uploading of files requires some necessary configuration like :An HTTP server that acts as a transaction between the user and the server. Access to the directory of cgi-bin that consists of the receiving script.

There are some scripts that are already available. Form for the implementation and the coding of it will be like:
<form method="post" enctype="multipart/form-data" action="up.cgi">
The form that has to be uploaded will be done by the following given code:
<input type=file name=upload><br>
This tag will contain the file name that has to be uploaded on the website.
Any remarks about the file will be written like:
<input type=text name=remark><br>
<input type=submit value=Press> This form will allow user to upload their own file in an easy way.
</form>
Write a program to include the custom button with the form
Custom button can be given just by putting the image with the button or by using any other button then normal. Usually the button is being made by the <input> tag like:
<input type= “submit” value= submit>

An image can be used for the custom button as an input type like:
<input type = ”image” value = submit>

The input in the image format defines the graphical button that has to be placed in the form of submit on the web site. Image input type return the x-y coordinates rather than the normal text as a value. The attributes of Value and Alt will be used to set the name value attribute. The example for the same will be given as:
<input type="image" name="submit" alt="submit" value="submit" src="submit.jpg">
How to prevent the display of “Getting framed in HTML?
Getting framed refers to the document that is being displayed in someone else's frameset in your HTML. This will be password protected and the permissions has to be taken before inserting the frameset. The framing of the document can be avoided by using TARGET=_top applied to all the links that will lead to the document that are outside the scope of a particular user without permission. A javaScript can be used that will automatically handle the request to remove the existing framesets. This can be given as:
<script type="text/javascript">
if (top.frames.length!=0)
{
    if (window.location.href.replace)
       top.location.replace(self.location.href);
    else
       top.location.href=self.document.href;
}
</script>
How to include a frameset inside another frameset?
One frameset can be defined inside another frameset if the accessing permission are provided directly. The frameset can be stored by using the JavaScript in the document that is being written by the user and the script is as follows:
<SCRIPT TYPE="text/javascript">
if (parent.location.href == self.location.href)
{
    if (window.location.href.replace)
       window.location.replace('frame.html');
    else
       // causes problems with back button, but works
       window.location.href = 'frame.html';
}
</SCRIPT>

The anchor <a> tag is used to link the frameset that can be used to restore the frames that has been stored.
<A HREF="frameset.html" TARGET="_top">Restore the frame

There is always a separate frameset document written for every content document. The frameset documents are generated automatically. The content document can be linked separately rather than linking them together.
How to update two frames at the same time using HTML?
To update the two frames at the same time there is a requirement for the HTML based techniques that links the documents with a new frameset document. It specifies a new frames that can be combined with other frames. There is a JavaScript that will be used to link the updated frame and the method that will be used is onClick(). HTML based technique allow the new frameset document with the attribute of TARGET=_top. In this the first frameset document uses a secondary frameset document that will be defined as the nested frameset. The following code explains it further:
<frameset cols="*,3*">
<frame src="first.html" name="first_frameset">
<frame src="second.html" name="sec_frameset">
<noframes>
</body></noframes>
</frameset>

The link that is given in the TARGET= “sec_frameset” attribute it replaces all the frames that is defined as second.html.

What are different ways to integrate a CSS into a Web page?
There are three ways to integrate CSS into a Web page

1) Inline : HTML elements may have CSS applied to them via the STYLE attribute.
2) Embedded : By placing the code in a STYLE element within the HEAD element.
3) Linked/ Imported : Place the CSS in an external file and link it via a link element.
If background and colour should always be set together, why do they exist as separate properties?
The reasons for this are as follows:

1. It increases the legibility of the style sheets. The background property is a complex property in CSS. If it is combined with color, the complexity will further increase.
2. Color is inherited, but background isn’t. This can further increase the confusion.
Explain external Style Sheet? How would you link to it?
1. External Style Sheet can be called as a template/document/file which contains style information and can be linked with more than one HTML documents.
2. Using this the entire site can be formatted and styles just by editing one file.
3. The file is linked with HTML documents via the LINK element inside the HEAD element.
<HEAD> <LINK REL=STYLESHEET HREF="style.css" TYPE="text/css"> </HEAD>
What are the advantages and disadvantages of External Style Sheets?
The advantages of External Style Sheets are:

1. Using them, the styles of multiple documents can be controlled from one file.
2. Classes can be created for use on multiple HTML element types in many documents.
3. In complex situations, selector and grouping methods can be used to apply styles.

The disadvantages of External Style Sheets are:

- In order to import style information for each document, an extra download is needed.
- Until the external style sheet is loaded, it may not be possible to render the document.
- For small number of style definitions, it is not viable.
What are the advantages and disadvantages of Embedded Style Sheets?
The advantages of Embedded Style Sheets are:

1. It is possible to create classes for use on multiple tag types in the document
2. Under complex situations, selector and grouping methods can be used to apply styles.
3. No extra download is required to import the information.

The disadvantages of Embedded Style Sheets are:

1. It is not possible to control the styles for multiple documents from one file, using this method.
What are the advantages and disadvantages of Inline Styles?
The advantages of Inline Styles are:

1. It is especially useful for small number of style definitions.
2. It has the ability to override other style specification methods at the local level.

The disadvantages of Inline Styles are:

1. It does not separate out the style information from content.
2. The styles for many documents can not be controlled from one source.
3. Selector grouping methods can not be used to handle complex situations.
4. Control classes can not be created to control multiple element types within the document.
How can you eliminate the blue border around linked images on web page?
This can be done by specifying the border property for linked images in your CSS as none:
For Example:
a img { border: none ; }

However, this makes it difficult for the users to differentiate between the clickable and non-clickable images.
What is CSS selector?
1. Basically it is a string that identifies the elements to which a particular declaration or set of declarations will apply.
2. It can also be referred to as a link between the HTML document and the style sheet.
3. It is equivalent of HTML elements.

For example:
A {text-indent: 12pt}

Here, the selector is A, which is called as type selector.
What is Tweening?
1. It is the short form for in-betweening.
2. It is the process of generating intermediate frames between two images.
3. It gives the impression that the first image has smoothly evolved into the second one.
4. It is an important method used in all types of animations.
5. In CSS3, Transforms(matrix,translate,rotate,scale etc) module can be used to achieve tweening.
Explain RWD.
1. RWD is the abbreviation for Responsive web design.
2. In this technique, the designed page is perfectly displayed on every screen size and device, be it desktop, mobile, laptop or any other device. You don’t need to create a different page for each device.
What is the use of CSS sprites?
1. A web page with large number of images takes a longer time to load. This is because each image separately sends out a http request.
2. The concept of CSS sprite helps in reducing this loading time for a web page by combining various small images into one image. This reduces the numbers of http request and hence the loading time.
What is the syntax to link external style sheet?
External style sheet are made up of css format only, it contains style information that can be linked with the HTML document externally. It is one of the easy and structured way as it keeps the style separate from the structure. It is a convenient way as only one file will be affected if any changes will be made overall. The file is linked through Link tag used inside the HTML Head.

The syntax is as follows:
<HTML>
<HEAD>
<LINK REL=STYLESHEET HREF="style.css" TYPE="text/css">
</HEAD>
</HTML>
How embedded style can be linked with HTML documents?
Embedded style is inside the HTML code only. It is written using the <Style> tag and used under the <Head> structure. It gets applied to the element for which the style will be written.

The syntax of it is as follows:
<HEAD>
<STYLE TYPE="text/css">
p {text-indent: 10pt;}
h1{text-color: #FFFFFF;}
</STYLE>
</HEAD>
Why imported is an easy way to insert the file?
Imported style sheet allows you to import the files which are external or combine one style sheet with another. There can be created many files, different style sheets to have different functions. Import function gives the provision to combine many elements or functionality into one. The syntax to import any file is @import notation, which is used inside the <Style> tag. There is a one rule that implies that the last imported sheet will override the previous ones.

The syntax is shown by coding as:
<Link Rel=Stylesheet Href="Main.Css" Type="Text/Css">
<STYLETYPE="text=css">
<!--
@import url(http://www.careerride.css);
@import url(http://www.carrerride.main.css);
.... your code
-->
</STYLE>

The <!-- --> is used as a comment for those browsers that doesn’t support css.
How do I combine multiple sheets into one?
Multiple sheets can be combined into by using the <link> tag and the with the title attribute. The title value allows one or more <link> tags to link with each other. After combination that theme will be applied as combined and will be shown to the user.

The syntax of it will be as follows:
<link rel= “text/css” href="default.css" title="combined">
<link rel= “text/css” href="style.css" title="combined">
<link rel= “text/css” href="para.css" title="combined">

Another way to combine the style sheets is the use of import which can be used in the <style> tag and the syntax can be given as follows:
@import url(site_url);
What are the rules in CSS ruleset?
CSS consists of two types of CSS rules, first is for ruleset which identifies the style and the selector. It combines the style and the selector.

1. Ruleset is a combination of CSS rules,
For Example : h1{text-color: 15pt;}, where this is the CSS rule.
2. Ruleset is selector + declaration
For Example : h1 + {text-color: 15pt;}

What is the CLASS selectors used for?
Class selectors are the selectors which are stand alone to a specific style that is declared. Class attribute can be used to declare the style and make an association with any HTML element.

The syntax for creation of class selector is: .classname.
The name can be from a-z, A-z or in digits.

The example code is shown as below:
.head{font: 12em;}, this is a class selector
<Body class= “head”> this is the class that is associated with the element </body>.
What is the difference between class selector and ID selector?
1. Class selector can be given to an overall block. This is sometimes termed as block element as well, whereas ID selector identifies a unique name and a style for a specific element.
2. ID selector declares the style for only one particular element which can be differentiated from other element, whereas Class selector is being given for the whole complete block.

Example of ID selector is being written like this:
#idname {color: red; background: black;}

This can be used in HTML as
<P ID= “idname”>this element only will be affected by the use of this ID element</P>
What is contextual selector?
Contextual selector specifies a specific occurrence of an element. It is combination of many selectors that are separated by white spaces. In this only the element that matches the specified element will be used not all the elements.

For example the syntax of it is being given as:
TD p code {color: #000000}

The element which is being defined as code will only be displayed as red as its color is being mentioned as red. But this is being done only if it occurs in the p text.
TD p code, h1, em {color: red}

The element code and em will only be displayed in red only when it occurs in h1 or p.
What do you understand by parent-child selector?
Parent-child selector represents the direct relationship between parent element and child element. It is been created by using two or more (~) tilde separated selectors.

For example:
Body ~ p {background-color: red; text: #FF00FF;}

Here the p element gets declared for a specific element and style only that element but if it has some child element then those elements will also get styled.

One more example to show the parent-child relationship as:
Body ~ p ~ em {background-color: red; text: #FF00FF;}

The syntax in HTML will be written as:
<body><p><em> It will show the two colors for em and p</em></p></body>
What is ‘important’ declaration used in CSS?
Important declarations are those declarations which have high weightage then normal declarations. These declarations override other declarations of less importance while executing. If suppose there are two statements from two users and both consist of important declaration then the one of the users declaration will override the another users declarations.

For example:
Body {background: #FF00FF !important; color: grey}

In this body background has more weight than the color.
Is there any provision to include one or more declaration in a selector?
There is a provision to include one or more declaration in a selector by using the semicolon as this shows the separation of the properties.

For example:
Selector {declaration1; declaration2}
P {background: white; color: black}
What is the use and syntax of class in CSS?
Class is a group of attributes and properties that uniquely identify style that can be attached to any element. It also defines instances for different element to which the same style can be attached.

The following example shows the use of class in CSS:
P {color:red} : It will display text color red in all paragraphs. This can be included with each element where the paragraph tag can be used. There can be given one style to one paragraph and another style to other paragraphs. A class may not have any association with the specific element. But any element with which the specific class is attached will have the same style.

For Example:

CSS
H1.prop1 {color: red} /* one class of P selector */
H2.prop2 {color: blue} /* another class of P selector */
.prop3 {color: green} /* can be attached to any element */

HTML
<h1 class=prop1>This paragraph will be red</P>
<h2 class=prop2>This paragraph will be blue</P>
<p class=prop3>This paragraph will be green</P>
<h3 class=prop3>This list item will be green</LI>
How grouping happens inside a CSS?
Grouping in CSS can be done by using the comma (,) separator in between one or more selectors that share the same style. A list of separator can be separated by using a semicolon as well.

For Example:
H1 {font-style: italic}
p.first {font-style: italic}
.name {font-style: italic}

In the above example all the css element share the same style so instead of writing like that it can be written as:
H1, p.first, .name {font-style: italic}

This reduces the size of the style sheet and also save the writing time for those sheets.
What is the purpose of pseudo-elements?
Pseudo elements allow the use of the part of element and not the element itself. They are applied to block level element, which is used for the complete block for which the CSS is being written. This allow the subpart of an element to be styled like paragraphs and headings.

For example:
selector:pseudo-element {property:value;}
p: first-line {text-transform: lowercase;}

It adds the style to the first line of the code in the paragraph.
How pseudo-classes are different from pseudo-elements?
Pseudo classes are used to add style and special effects to some selectors which is being used inside some class.

The syntax it as follows
selector:pseudo-class {property:value;}
a:link {color:#FF0000;}

pseudo classes can be combined with other classes as well.
The syntax of it will be shown as:
selector.class:pseudo-class {property:value;}
a.red:visited {color:#FF0000;}
What does cascade and cascading order defines?
Cascade is a method in CSS that defines the importance of particular style rules. This doesn’t allow any conflict to occur between other elements that is being defined within the same CSS. Declaration with more importance get executed first then others.

The syntax is as follows:
Selector{property: value ! important} /* increased weight */
selector (property: value} /* normal weight */

Cascading order is a sorting method that consists of some rules of the declarations through which it can be sorted and the conflict can be resolved which might occur between it. In this all the declarations has to be found that apply the selector and properties to a specific elements.
What are the different sorting methods used inside the cascading order?
Cascading order is a sorting method that allows many different sorting methods like:

1. Sort by origin : In this some rules will be defined like:
- Normal weight in provider’s style sheet will override the style sheet rules of the user’s.
- Increased weight in user’s style sheet will override normal weight of style sheet of provider.

2. Sort by selector's specificity : In this more specific selector will override the selectors that are less specific: For Example:
- ID selector is the most specific one.
- Contextual selectors are less specific.
- So, ID selector will override the contextual selector style sheets.

3. Sort by order specified : If two selectors are same in the weight and other properties then the specification will be seen for overriding.
For Example:
- Style attribute used for inline style will override all other styles.
- Link element used for external style will override imported style.
How inline and block elements are different from each other?
1. Inline elements don’t have line breaks. An Inline element doesn’t have elements to set width and height.
For Example: em, strong, etc. codes are few examples of inline elements.

2. Block elements do have line breaks and they define the width by setting a container. It also allowed setting height. It can contain the elements that occur in inline elements.

For Example:
width and height
max-width and max-height
min-width and min-height
hi (i=1-6)- heading element
p- paragraph element.
How does inheritance work in CSS?
Inheritance is a concept that is used in HTML and other languages but it is used in CSS as well to define the hierarchy of the element from top level to bottom level. In inheritance child will inherit the properties of parent. In this the restriction is being applied that not all the properties can be applied. Inheritance passes its properties to its children class so that the same property doesn’t have to define the same property. Inherited properties can be overrided by the children class if child uses the same name properties.

For Example:
Body {font-size: 10pt;}

And another definition is being defined in the child class
Body {font-size: 10pt;}
H1 {font-size: 14pt;}

All the paragraph text will be displayed using the property defined in the body except for the h1 style which will show the text in font 14 only.
What are the advantages of the external over inline style methods?
1. External Style Sheets are useful as it keeps the style and content separately and doesn’t allow it to mix with each other. It can control the styles for multiple documents, whereas inline style mixes the content with the style and make the code messier.
2. External style sheet allows the creation of various classes in a structured way, whereas inline style sheet can’t create or control class elements.
3. External style sheet can use selector and grouping methods to apply styles, whereas inline styles can’t use selector and grouping methods.
How do you override the underlining of hyperlinks?
The concept of override the underlining of hyperlinks in CSS is done by using control statements and using external style sheet.

For Example:
A { text-decoration: none; }

Suppose this is being written in CSS file and in the anchor tag in HTML the format is being written as:
<a href="career.html" style="text-decoration: none">link text</a>

So, anything thing written as inline will override the style for the hyperlink used in external style sheet.
How to center the block-elements with CSS?
CSS allows you to style your web-pages and sheets so that you can visualize it in better way.

This can be done in two ways:
1. It can be done by defining the properties like margin-left and right to auto and width can be given any value.
For Example:
body {width: 30em; background: cyan;}
h1 {width: 22em; margin-left: auto; margin-right: auto}

2. It can be done by the use of table like:
Table {margin-left: auto; margin-right: auto; width: 400px;}

This table width is being defined by the content used. These are the methods that are used to center the block element.
What will happen if we will use floats across the page with 100% width?
In CSS if float declaration is being made then it add some width in the form of border and it allow it to float even more. So, the width can be used just by adding the border of say 1 pixel in CSS element.
What is the Difference between id and class?
The id and class is being used in HTML and includes the values from CSS. The difference is as follows:

1. Id is an attribute that it uniquely assigns a name to a particular element, whereas class defines an element with certain set of properties which can be used for a complete block.
2. Id can be used for an element and uniquely identifies it, whereas class is used as block element and applied to many tags where it is used.
3. Id restricts the use of properties to one specific element, whereas class applies the rules and properties to specific block or group of elements.
How to restore the default property value using CSS?
CSS doesn’t provide any default values that can be used if the user wants to revert back to the old values. The only option which can be performed to restore the default property value is to re-declare the property which you want to revert back to. Rules should be defined for using the selectors like tag name, etc. that you want to override for more specific values.
What is the purpose of Nesting Selectors?
Nesting selectors are the selectors that define a selector inside another selector.

For Example:
H1
{color:blue;
text-align:center;}
.marked
{background-color:red;}
.marked h1
{color:white;}

In this a particular style is being defined for the element of h1, and another is given for all other elements. Here the class is given as “marked” and one more style given for h1 element within the h1 style.
How CSS float works?
CSS float is useful when you don’t have to give width for an element or you don’t want to keep the element fixed. It allows the elements to be given left or right boundaries to expand and wrap all other elements. Float is basically used for images and for layouts. Elements in this can be made float horizontally i.e. left or right.

For Example:
img{float:right;}
What is the use of Media Types in CSS?
Media types in CSS define the media like audio and video to be used in your HTML document to represent the properties in a better way. The font property can be used for media types as it can be used for print media or screen media. Document requires a defined media to represent the screen that can be read on the paper. It is used as:@media
<html>
<head>
<style>
@media screen
{
    p.test {font-family:verdana,sans-serif;font-size:14px;}
}
@media print
{
    p.test {font-family:times,serif;font-size:10px;}
}
</style>
</head>
<body>
----------Your code here----------
</body>
</html>
What are the different Media Types included in CSS?
Media types are not case sensitive and it allows you to define different properties in different media.

The different media type that is included in CSS is:

1. Aural – Used for speech and sound synthesizers
2. Print – Used to show the content as they will look when you will use the print command
3. Projection - Used to show the CSS for the projectors
4. Handheld - Used for handheld devices
Used for screens like computers and laptop
Why CSS Box Model is used? What are the elements that it includes?
CSS box model defines the design and layout of the styling element. It is a box that shows the elements that will come before others. Like, it consists of margins, borders, padding, and the actual content. It allows a structured way to show the elements in comparison to other elements.

The terms that are used in box model is shown as:

1. Margin – It shows the top most layer and it shows the overall structure which consists of border and other elements that is being shown below.
2. Border – It shows the padding and content option and keep a border around it. Border can be affected by background color.
3. Padding – It shows the space between the content blocks. It is affected by the background color.
4. Content –. It shows the actual content like text and images. These all are essential terms that allows you to understand the structure and apply it to your code.
Write the css code showing the usage of all the background properties.
With the help of css there are several ways to change the background properties of an html page. For ex. the following code will place the background image at the center of the body element. Also the background would not be repeated and the scroll would be locked.
BODY
{
    font-family : "Verdana, Arial, Helvetica, sans-serif;
    background-image: url(images/background_image.gif);
    background-repeat: no-repeat;
    background-position: center;
    background-attachment: fixed;
    background-color: #FF00FF;
    color : #FF0000;
    margin: 20px;
}
How are contextual selectors used in CSS?
The contextual selector is a special type of selector that is used to select special occurrences of an element. This selector is a string of individual selectors separated by spaces. It defines a search patterns of the element where only the last element in the pattern is addressed to.

For Example:
TD P TEXT {color: blue}

This implies that the TEXT will appear blue in color only if it occurs in the context of the element P which itself occurs in the context of TD.
P.about {color: red}

This implies that any element specified with class .about will appear in red color but only if it occurs in context to P.
How can the same properties be defined for different elements without repeating them again and again? Explain with an example:
In order to specify the same style properties for multiple elements in css we can make use of class. Class in general are a group of of instances of the same elements to which the same style can be assigned or it can be a group of different instances to which a common style can be assigned.

For Example:

CSS code
P.class1 {color: red} /* defines a class of P selector */
P.class2 {color: blue} /* defines another class of P selector */
.class3 {color: green} /*this class can be used with any element*/

HTML code
<P class=class1>This paragraph will be colored in red</P>
<P class=class2>This paragraph will be colored in blue</P>
<P class=class3>This paragraph will be shown in green</P>
<LI class=class3>This list item will also be green</LI>
How can imported style sheets be linked? Explain with the help of an example?
- Imported style sheets are those style sheets which as their name suggests can be combined for use with another sheet. By doing so the designer is able to create a single main sheet which has declarations that apply to the whole site and specific style sheets that apply only to certain specific elements.
- In order to import a style sheet the style element must contain the @notation. In case of multiple sheets being imported they will be done so in the order they are imported. The last imported sheet would over write any previous style sheet property.

For Example:
<LINK REL=STYLESHEET HREF="major.css" TYPE="text/css">< BR><STYLETYPE="text=css">
<!--
@import url(http://www.css.stylesheet1.css);
@import url(http://www.css.stylesheet2.css);
-->
</STYLE>
Explain with the help of an example the usage of a parent-child selector.
The parent-child selector as the name suggests is used for selecting the direct descendent of a parent element. This selector is represented by using the “~” tilde symbol between two selectors.

For Example:
body ~ li {background: blue; color: red}

This specifies that the LI element will be declared the above style rules only when the LI would be a descendant of the BODY element.
body ~ li ~ em {background: blue; color: white}

In this example the em will be specified the above properties only when it is a descendant of li which itself is a child of body. The parent child selector can be used to specify a particular element when there are multiple instances of the same element.
Why should inline styles be used carefully?
Inline style rules allows a user to attach individual styles to individual elements in an HTML document. The syntax of an inline style rule attached to an HTML element:
<p style=”color: red;”> Red text</p>

Inline styles are generally not the preferred way of applying a style rule and must be used carefully because of the following reasons:

1. The style rules can easily get mixed up in an HTML page code.
2. The entire rule must be specified in the value of the style attribute, this can be tough in case of long rules.
3. By using inline styles the user is unable to take advantage of CSS properties such as grouping selectors and re usability of a style sheet.
4. It is generally advised to use either internal or external style sheets as they are more convenient to manage and can be changed easily as they are at the same place.
How do hexadecimal color codes differ from RGB values?
In CSS a user can specify a color in two ways:

1. Hexadecimal color codes : These as their name suggest use six characters to represent a color. It is a combination of numbers and letters. When you use a hexadecimal code to specify a color it should always be precede by a “#”. This ensures that the color is displayed correctly in a browser.
Example :
p {color: #0000FF;}

2. RGB color values : Every color can be defined as a mixture of red, green and blue. In CSS the user can also define the value of a color by specifying the RGB values in two different ways:

- rgb(r,g,b) : In this type the values can be in between the integers 0 and 255.
- rgb(r%,g%,b%) : The rgb basically represent the percentage of red, green and blue of the color.

The hexadecimal values of a color are the ones that are most widely used.
What is the use of a pseudo class? Explain with the help of an example?
The pseudo classes are used to define the css properties of an element that does not exist otherwise. Pseudo classes enables the user to define the style properties of an element which otherwise would not have been possible. The pseudo class name is always preceded by a colon “ : ”.

Pseudo classes can be used with:

1. Elements
2. Classes
3. ID`s

Some of the common pseudo classes that are used with hyperlink are:

1. link defines the properties of the link that have not been visited.
2. visited defines the properties if the links that have been visited.
3. hover defines the properties of the link when the mouse cursor hovers on them.

For Example:
a:link {color: black;}

This will set the color of any hypelink that points to an unvisited link and will appear in black color.
How is a CSS executed in case of more than one conflicting rule?
If there are two or more css rules which are pointing towards the same element there are some basic rules that a browser follows in order to know which is the most specific and will be executed / applied.

For Example:
p {color: red;}
p {color: blue;}

In the above case all the p contents would appear blue as this rule was specified the last.
In css every element is assigned a unique specificity value. Based on the specificity value a style rule is executed.

For Example:
p : this has the specificity of 1
div p : this has a specificity of 2 ( ie 1 + 1 of two selectors )
.class : has a specificity of 10
#id : This has a specificity of 100.

In this way whichever selector has the highest specificity will apply in case of multiple selectors pointing at the same element.
Explain with the help of examples how the display property is used in CSS.
In CSS the user has the ability to define how the content will be displayed. There are three fundamental types of display:

1. Inline : The elements are displayed in a line.
2. Block : In this display style a line break is placed before and after every element.
3. None : Does not display the elements.

The syntax of specifying a display style is :
h1 { display: inline; }

CSS provides the user with further more display styles such as:

1. list-item : Does the same work as the HTML li element. Displays the content in a list.
2. marker : This property is exclusively used with the pseudo elements :before and :after.
3. Tables : The table properties can be used in similar way to the table elements provided by HTML but css further extends the functionality by providing properties like table-column, table-caption etc.

For Example:
div.test
{
    display:inline;
    zoom:1.0;
}
Explain what are image sprites and how are they used in css.
Image sprites are basically a collection of images put into a single image. A web page can contain multiple images and loading them all one by one can be a slow process. By using image sprites only a single image is used and by specifying the area of the image to be displayed the same image can be used multiple times.
For ex : We have a an image.gif which contains the home, forward and back navigation buttons. With the help of css the user can simply specify only the part of the image that is needed. Now the user wants to only display the home part of the image for the home button.

CSS code:
img.home
{
    width:50px;
    height: 44px;
    background: url (image.gif) 0 0 ;
}

In the above css code only a part of the overall image.gif will be used, in this case the home page button area only. By using image sprites the page loading time can be reduced by substantial margins. The user only needs to know absolute image area to be dispalyed.
With the help of examples explain grouping and nesting of css selectors.
Grouping selectors : In css the designer can reduce the code by simply groping together selectors with the same property values.

For Example:
h1 {color: green;}
h2 {color: green;}
p {color: green;}

As you can see from the above code the all the elements have the same property. To avoid rewriting the same code again and again the user can simply group the selectors by separating each selector with a comma.
Grouped selectors :
h1,h2,p {color: green;}

Nesting selectors : This enables the user to specify a style for a selector within a selector.
For Example:
p
{
color:blue;
text-align:center;
}
.marked
{
background-color:red;
}
.marked p
{
color:white;
}

In the above example separate properties are assigned for p and the .marked class. But the last value that is .marked p implies that the property will apply to p elements with class defined as .marked.
How can HTML elements be styled having specific attributes?
Css allows the user to style the html elements that have specific attributes. It does not only rely on class and id.

For Example:
[title]
{
color:red;
}

This will simply color any attribute containing title.
Css also allows the user to specify an attribute with a particular value.
For Example:
[title=test]
{
color:red;
}

This will simply color the text test that appears anywhere in the title attribute.
Also the user can specify an attribute with multiple values.
For Example:
[title~=test] {color:blue;}
What are the different provision provided in css to define the dimension of an element?
In css the user can choose from multiple dimension properties to style an element. The list of css dimension properties are:

1. height : This property allows the user to specify the height of a specific element.
2. max-height : This allows the user to set the maximum height of an element.
3. max-width : This specifies the maximum width of an element.
4. min-height : It allows the user to specify the minimum height of an element.
5. min-width : Used to set the minimum width of an element.
6. width : This property is used to set the width of an element.

For Example:
img.big {height:100px} <!-- specifies the height of an element-->
img.big {max-height:100px} <!-- specifies the maximum height of an element-->
Explain the concept of the box model in css.
CSS uses the concept of a box model which implies that every HTML element is a box. This term is used when we are talking about design and layout. The CSS box model is actually a box that wraps an HTML element.

A box comprises of the following components:

1. margins : Used to clear an area around a border.
2. border : Border goes around the padding and the content.
3. padding : Used to clear the area around the content.
4. content : This contains the actual content of the box that is the text and the images.

It is important to note that when a user sets the height and width of an element, they are doing so only for the content area. To know the fill size of the element the user must also specify the other layers i.e. the padding border and margins.

For Example:
p
{
    width:220px;
    padding:10px;
    border:5px solid gray;
    margin:0px;
}

The total width of an element is calculated like this:
Total element width = width + left padding + right padding + left border + right border + left margin + right margin

The total height of an element is calculated like this:
Total element height = height + top padding + bottom padding + top border + bottom border + top margin + bottom margin
How is the float property implemented in css?
The css float property allows an element to be pushed to the left or right which allows other elements to wrap around the floated element. The elements specified before the float element will not be effected. Only the elements specified after the floated elements will float around the element.

For Example:
img { float:right;}

This implies that if an image is floated towards the right then the text that follows its would flow around it on the left. The user can also float multiple elements together. The elements would float if there is space available for them to float. Any float element will cause the other elements following it to float around it, to avoid this the user can make use of the clear property. The clear property is used to specify the sides of an element on which the floating of elements is not allowed.

For Example:
.line {clear:both;}

This would prevent the elements from floating around after the float element.
What is the purpose of the z-index? Explain with the help of an example.
While using css to position html elements they may overlap each other. The z index i used to specify which element overlaps which element. The z-index is a number which can either have a positive or a negative value. By default the z-index value is zero. In case elements have the same z-index number specified then the browser will layer them according to the order in which they appear in the HTML.

For Example:
We have a list of 4 elements each with their defined numbers:
element1 - z-index number 25
element2 - z-index number -34
element3 - z-index number 10
element4 - z-index number not defined
In this case the order of their stack would be:
element1
element3
element4
element2
Explain the meaning of graceful degradation in reference to CSS.
Generally graceful degradation is a concept that allows a system to continue to operate properly in the event of a failure of a component. In web design the graceful degradation is a very important area. When a developer creates a website he creates it to take advantage of the latest browser support etc. but care should also be taken to render the website properly on older browsers. In this way the designer is able to get a wider audience by stepping down some of the features to provide basic functionality to people with older browsers. For example while specifying an image in the html css code many time an alt tag is used. This means that in case the image cannot be shown in a browser it will instead show the text specified within the alt tag.
What is the other alternative to graceful degradation?
The other concept is know as progressive enhancement. Progressive enhancement focuses on the content of a web rather than the browsers itself. In this way a website can be viewed on different platforms according to the amount of resources available. For ex a user with the latest browser and a high bandwidth connection might get some extra eye candy as compared to a user visiting the same site on a dial-up and old browser. But the overall functionality provided would be the same. Gmail does so as well where users with slow connections are provided a plain html view whereas high bandwidth users get the complete site to access. This concept recently has come into play as mobile devices with Internet surfing capabilities have started to grow and expand its user base.
How are shorthand properties are used in css? Give examples.
One of the primary advantages of css is that it greatly reduces page load times. Writing multiple properties and their values in a single line of css code is known as css shorthand technique. One thing to be kept in mind is that while using the css shorthand technique is that the order of specifying the values of an attribute must be maintained. In case the user wants to keep a value as default it is not needed to be mentioned.

For Example:
margin-top: 5em;
margin-bottom: 3em;
margin-right: 1em;
margin-left: 1em
Becomes:
margin: 5em 1em 3em (top, right and left, bottom);

border-width:5px;
border-style:solid;
border-color:#fff;
Becomes:
border:5px solid #fff;
1. What is JavaScript?
Ans: JavaScript is a single-threaded programming language that we can use for client-side or server-side development. It is a dynamically typed programming language, which means that we dont care about variable data types while writing the JavaScript code. Also, it contains the control statements, operators, and objects like Array, Math, Data, etc.

2. What are the advantages and disadvantages of JavaScript?
Ans: Every language has pros and cons and JavaScript is no different from others.

Advantages of JavaScript
Less server interaction: You can validate user input before sending the page off to the server. This saves server traffic, which means less load on your server.
Immediate feedback to the visitors: They don't have to wait for a page reload to see if they have forgotten to enter something.
Increased interactivity: You can create interfaces that react when the user hovers over them with a mouse or activates them via the keyboard.
Richer interfaces: You can use JavaScript to include such items as drag-and-drop components and sliders to give a Rich Interface to your site visitors.
Disadvantages of JavaScript
We can not treat JavaScript as a full fledged programming language. It lacks the following important features.

Client-side JavaScript does not allow the reading or writing of files. This has been kept for security reason.
JavaScript can not be used for Networking applications because there is no such support available.
JavaScript doesn't have any multithreading or multiprocessor capabilities.
3. Is JavaScript a case-sensitive language?
Ans: Yes! JavaScript is a case-sensitive language. This means that language keywords, variables, function names, and any other identifiers must always be typed with a consistent capitalization of letters.

4. What are the variable naming conventions in JavaScript?
Ans: While naming your variables in JavaScript keep following rules in mind.

You should not use any of the JavaScript reserved keyword as variable name. You can check all the reserved keywords.
JavaScript variable names should not start with a numeral (0-9). They must begin with a letter or the underscore character. For example, 123test is an invalid variable name but _123test is a valid one.
JavaScript variable names are case sensitive. For example, Name and name are two different variables.
5. How typeof operator works?
Ans: The typeof is a unary operator that is placed before its single operand, which can be of any type. Its value is a string indicating the data type of the operand.

The typeof operator evaluates to "number", "string", or "boolean" if its operand is a number, string, or boolean value and returns true or false based on the evaluation.

6. How to create an Array in JavaScript?
Ans: You can define arrays using the array literal as follows

var x = [];
var y = [1, 2, 3, 4, 5];
7. How to read elements of an array in JavaScript?
Ans: An array has a length property that is useful for iteration. We can read elements of an array as follows.

var x = [1, 2, 3, 4, 5];
for (var i = 0; i < x.length; i++) {
   // Do something with x[i]
}
To know morea about JavaScript array check the attached link.

8. How to create an Object in JavaScript?
Ans: JavaScript supports Object concept very well. You can create an object using the object literal as follows.

var emp = {
   name: "Zara",
   age: 10
};
9. How to read properties of an Object in JavaScript?
Ans: You can write and read properties of an object using the dot notation as follows.

// Getting object properties
emp.name            // ==> Zara
emp.age             // ==> 10

// Setting object properties
emp.name = "Daisy"  // <== Daisy
emp.age  =  20      // <== 20
To know more about the JavaScript object please check the attached link.

What are the different data types in JavaScript?
Ans: JavaScript data types can be categorized as primitive and non-primitive.

Primitive: Predefined data types by JavaScript is know as primitive data types like -
Numbers
Strings
Boolean
Symbol
Undefined
Null
BigInt
Non-Primitive: These data types are derived from primitive data types.
Objects
Functions
Arrays
Intermediate Level JavaScript Interview Question
1. What are the valid scopes of a variable in JavaScript?
Ans: The scope of a variable is the region of your program in which it is defined. JavaScript variable will have only two scopes.

Global Variables: A global variable has global scope which means it is visible everywhere in your JavaScript code.
Local Variables: A local variable will be visible only within a function where it is defined. Function parameters are always local to that function.
2. Which type of variable among global and local, takes precedence over other if names are same?
Ans: A local variable takes precedence over a global variable with the same name.

3. What is a named function in JavaScript? How to define a named function?
Ans: A named function has a name when it is defined. A named function can be defined using function keyword as follows.

function named(){
   // do some stuff here
}
4. How many types of functions JavaScript supports?
Ans: A function in JavaScript can be either named or anonymous.

To know more abut the JavaScript functions please check the attached link.

5. How to define a anonymous function?
Ans: An anonymous function can be defined in similar way as a normal function but it would not have any name.

// Named function
function namedFunction() {
    return "I have a name";
}

// Anonymous function
const anonymousFunction = function() {
    return "I don't have a name";
};
6. Can you assign a anonymous function to a variable?
Ans: Yes! An anonymous function can be assigned to a variable.

7. What is the purpose of 'this' operator in JavaScript?
Ans: JavaScript 'this' keyword contains the reference to the object. It represents the context of the function or current code. It is used to access the properties and methods of the current object.

8. What is Date object in JavaScript?
Ans: The Date object is a datatype built into the JavaScript language. Date objects are created with the new Date( ).

Once a Date object is created, a number of methods allow you to operate on it. Most methods simply allow you to get and set the year, month, day, hour, minute, second, and millisecond fields of the object, using either local time or UTC (universal, or GMT) time.

9. What is Number object in JavaScript?
Ans: JavaScript Number object represents numerical date, either integers or floating-point numbers. In general, you do not need to worry about Number objects because the browser automatically converts number literals to instances of the number class.

Syntax: Creating a number object

var val = new Number(number);
If the argument cannot be converted into a number, it returns NaN (Not-a-Number)

10. Which built-in method reverses the order of the elements of an array?
Ans: JavaScript reverse() method reverses the order of the elements of an array The first becomes the last, and the last becomes the first.

11. How to redirect a url using JavaScript?
Ans: To redirect using JavaScript at client side. To redirect your site visitors to a new page by using following ways.

// Simulate a mouse click:
window.location.href = "https://www.tutorialspoint.com/";

// Simulate an HTTP redirect:
window.location.replace("https://www.tutorialspoint.com/");
12. How to print a web page using JavaScript?
Ans: JavaScript helps you to implement this functionality using print function of window object. The JavaScript print function window.print() will print the current web page when executed.

<html>
   <head>
      <title>Print Page</title>
      <script>
         function printpage() {
            window.print();
         }
      </script>
   </head>
   <body>
      <h2>This is a sample page to print</h2>
      <button onclick="printpage()">Print Page</button>
   </body>
</html>
13. What typeof returns for a null value?
Ans: It returns "object".

14. How to dynamically create new elements in JavaScript?
Ans: We will have a button element and on clicking it, we will generate a new p element and append it to the DOM.

<body>
       <h3>How to dynamically create new elements in JavaScript?</h3>
       <div id="container">
       <!-- Newly created elements will be appended here -->
    </div>
    <button onclick="createNewElement()">Create Element</button>

    <script>
       function createNewElement() {
       // Create a new paragraph element
       var newParagraph = document.createElement('p');

       // Set the text content of the paragraph
       newParagraph.textContent = 'This is a dynamically created paragraph.';

       // Append the paragraph to the container div
       var container = document.getElementById('container');
       container.appendChild(newParagraph);
       }
    </script>
</body>
15. What is Function Hoisting?
Ans: The function hoisting in JavaScript is a default behavior in which function declarations are moved at the top of their local scope before execution of the code.

Advanced Level JavaScript Interview Question
1. What is callback?
Ans: A callback is a plain JavaScript function passed to some method as an argument or option. Some callbacks are just events, called to give the user a chance to react when a certain state is triggered.

2. What is closure?
Ans: Closures are created whenever a variable that is defined outside the current scope is accessed from within some inner scope.

<body>
   <p id = "demo"> </p>
   <script>
      const output = document.getElementById("demo");
      function outer() {
         output.innerHTML += "The outer function is executed! <br>";
         function inner() {
            output.innerHTML += "The inner function is executed! <br>";
         }
         inner();
      }
      outer();
   </script>
</body>
3. What is arguments object in JavaScript?
Ans: JavaScript variable arguments represents the arguments passed to a function.

4. How can you get the type of arguments passed to a function?
Ans: Using typeof operator, we can get the type of arguments passed to a function.

function func(x){
   console.log(typeof x, arguments.length);
}
func();                //==> "undefined", 0
func(1);               //==> "number", 1
func("1", "2", "3");   //==> "string", 3
5. How can you get the total number of arguments passed to a function?
Ans: Using arguments.length property, we can get the total number of arguments passed to a function.

function func(x){
   console.log(typeof x, arguments.length);
}
func();                //==> "undefined", 0
func(1);               //==> "number", 1
func("1", "2", "3");   //==> "string", 3
6. How can you get the reference of a caller function inside a function?
Ans: The arguments object has a callee property, which refers to the function you're inside of.

function func() {
   return arguments.callee; 
}
func();
7. Can you pass a anonymous function as an argument to another function?
Ans: Yes! An anonymous function can be passed as an argument to another function.

8. How to handle exceptions in JavaScript?
Ans: The latest versions of JavaScript added exception handling capabilities. JavaScript implements the try...catch...finally construct as well as the throw operator to handle exceptions.

You can catch programmer-generated and runtime exceptions, but you cannot catch JavaScript syntax errors.

9. What is purpose of onError event handler in JavaScript?
Ans: The onError event handler was the first feature to facilitate error handling for JavaScript. The error event is fired on the window object whenever an exception occurs on the page.

The onError event handler provides three pieces of information to identify the exact nature of the error. Please check JavaScript - Errors & Exceptions Handling.

Error message: The same message that the browser would display for the given error.
URL: The file in which the error occurred.
Line number: The line number in the given URL that caused the error.
10. Can you access Cookie using JavaScript?
Ans: JavaScript can also manipulate cookies using the cookie property of the Document object. JavaScript can read, create, modify, and delete the cookie or cookies that apply to the current web page.

11. How to create a Cookie using JavaScript?
Ans: The simplest way to create a cookie is to assign a string value to the document.cookie object.

document.cookie = "key1 = value1; key2 = value2; expires = date";
12. How to read a Cookie using JavaScript?
Ans: Reading a cookie is just as simple as writing one, because the value of the document.cookie object is the cookie. So you can use this string whenever you want to access the cookie.

The document.cookie string will keep a list of name = value pairs separated by semicolons, where name is the name of a cookie and value is its string value.

You can use strings' split() function to break the string into key and values.

13. How to delete a Cookie using JavaScript?
Sometimes you will want to delete a cookie so that subsequent attempts to read the cookie return nothing. To do this, you just need to set the expiration date to a time in the past.

To know all about Cookies please click on attached link.

14. What will be the output order and why?
console.log('1');

setTimeout(() => {
    console.log('2');
    Promise.resolve().then(() => {
        console.log('3');
    });
}, 0);

Promise.resolve().then(() => {
    console.log('4');
    setTimeout(() => {
        console.log('5');
    }, 0);
});

console.log('6');
Output: First, synchronous code execution prints 1 and 6 the the first Promise microtask queues up and prints 4. After 4, a new setTimeout is queued and original setTimeout executes and prints 2. Promise within first setTimeout prints 3 and finally, last setTimeout executes and prints 5

1, 6, 4, 2, 3, 5
Explain event delegation
Event delegation is a technique involving adding event listeners to a parent element instead of adding them to the descendant elements. The listener will fire whenever the event is triggered on the descendant elements due to event bubbling up the DOM. The benefits of this technique are:

Memory footprint goes down because only one single handler is needed on the parent element, rather than having to attach event handlers on each descendant.
There is no need to unbind the handler from elements that are removed and to bind the event for new elements.
References
https://davidwalsh.name/event-delegate
https://stackoverflow.com/questions/1687296/what-is-dom-event-delegation
Explain how this works in JavaScript
There's no simple explanation for this; it is one of the most confusing concepts in JavaScript. A hand-wavey explanation is that the value of this depends on how the function is called. I have read many explanations on this online, and I found Arnav Aggrawal's explanation to be the clearest. The following rules are applied:

If the new keyword is used when calling the function, this inside the function is a brand new object.
If apply, call, or bind are used to call/create a function, this inside the function is the object that is passed in as the argument.
If a function is called as a method, such as obj.method() — this is the object that the function is a property of.
If a function is invoked as a free function invocation, meaning it was invoked without any of the conditions present above, this is the global object. In a browser, it is the window object. If in strict mode ('use strict'), this will be undefined instead of the global object.
If multiple of the above rules apply, the rule that is higher wins and will set the this value.
If the function is an ES2015 arrow function, it ignores all the rules above and receives the this value of its surrounding scope at the time it is created.
For an in-depth explanation, do check out his article on Medium.

Can you give an example of one of the ways that working with this has changed in ES6?
ES6 allows you to use arrow functions which use the enclosing lexical scope. This is usually convenient, but does prevent the caller from controlling context via .call or .apply—the consequences being that a library such as jQuery will not properly bind this in your event handler functions. Thus, it's important to keep this in mind when refactoring large legacy applications.

References
https://codeburst.io/the-simple-rules-to-this-in-javascript-35d97f31bde3?gi=86e207b492c4
https://stackoverflow.com/a/3127440/1751946
Explain how prototypal inheritance works
All JavaScript objects have a __proto__ property with the exception of objects created with Object.create(null), that is a reference to another object, which is called the object's "prototype". When a property is accessed on an object and if the property is not found on that object, the JavaScript engine looks at the object's __proto__, and the __proto__'s __proto__ and so on, until it finds the property defined on one of the __proto__s or until it reaches the end of the prototype chain. This behavior simulates classical inheritance, but it is really more of delegation than inheritance.

Example of Prototypal Inheritance
// Parent object constructor.
function Animal(name) {
  this.name = name;
}

// Add a method to the parent object's prototype.
Animal.prototype.makeSound = function () {
  console.log('The ' + this.constructor.name + ' makes a sound.');
};

// Child object constructor.
function Dog(name) {
  Animal.call(this, name); // Call the parent constructor.
}

// Set the child object's prototype to be the parent's prototype.
Object.setPrototypeOf(Dog.prototype, Animal.prototype);

// Add a method to the child object's prototype.
Dog.prototype.bark = function () {
  console.log('Woof!');
};

// Create a new instance of Dog.
const bolt = new Dog('Bolt');

// Call methods on the child object.
console.log(bolt.name); // "Bolt"
bolt.makeSound(); // "The Dog makes a sound."
bolt.bark(); // "Woof!"

Things to note are:

.makeSound is not defined on Dog, so the engine goes up the prototype chain and finds .makeSound off the inherited Animal.
Using Object.create to build the inheritance chain is no longer recommended. Use Object.setPrototypeOf instead.
References
http://dmitrysoshnikov.com/ecmascript/javascript-the-core/
https://www.quora.com/What-is-prototypal-inheritance/answer/Kyle-Simpson
https://davidwalsh.name/javascript-objects
https://crockford.com/javascript/prototypal.html
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain
What do you think of AMD vs CommonJS?
Both are ways to implement a module system, which was not natively present in JavaScript until ES2015 came along. CommonJS is synchronous while AMD (Asynchronous Module Definition) is obviously asynchronous. CommonJS is designed with server-side development in mind while AMD, with its support for asynchronous loading of modules, is more intended for browsers.

I find AMD syntax to be quite verbose and CommonJS is closer to the style you would write import statements in other languages. Most of the time, I find AMD unnecessary, because if you served all your JavaScript into one concatenated bundle file, you wouldn't benefit from the async loading properties. Also, CommonJS syntax is closer to Node style of writing modules and there is less context-switching overhead when switching between client side and server side JavaScript development.

I'm glad that with ES2015 modules, that has support for both synchronous and asynchronous loading, we can finally just stick to one approach. Although it hasn't been fully rolled out in browsers and in Node, we can always use transpilers to convert our code.

References
https://auth0.com/blog/javascript-module-systems-showdown/
https://stackoverflow.com/questions/16521471/relation-between-commonjs-amd-and-requirejs
Explain why the following doesn't work as an IIFE: function foo(){ }();. What needs to be changed to properly make it an IIFE?
IIFE stands for Immediately Invoked Function Expressions. The JavaScript parser reads function foo(){ }(); as function foo(){ } and ();, where the former is a function declaration and the latter (a pair of parentheses) is an attempt at calling a function but there is no name specified, hence it throws Uncaught SyntaxError: Unexpected token ).

Here are two ways to fix it that involve adding more parentheses: (function foo(){ })() and (function foo(){ }()). Statements that begin with function are considered to be function declarations; by wrapping this function within (), it becomes a function expression which can then be executed with the subsequent (). These functions are not exposed in the global scope and you can even omit its name if you do not need to reference itself within the body.

You might also use void operator: void function foo(){ }();. Unfortunately, there is one issue with such approach. The evaluation of given expression is always undefined, so if your IIFE function returns anything, you can't use it. An example:

const foo = void (function bar() {
  return 'foo';
})();

console.log(foo); // undefined

References
https://lucybain.com/blog/2014/immediately-invoked-function-expression/
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void
What's the difference between a variable that is: null, undefined or undeclared? How would you go about checking for any of these states?
Undeclared variables are created when you assign a value to an identifier that is not previously created using var, let or const. Undeclared variables will be defined globally, outside of the current scope. In strict mode, a ReferenceError will be thrown when you try to assign to an undeclared variable. Undeclared variables are bad just like how global variables are bad. Avoid them at all cost! To check for them, wrap its usage in a try/catch block.

function foo() {
  x = 1; // Throws a ReferenceError in strict mode
}

foo();
console.log(x); // 1

A variable that is undefined is a variable that has been declared, but not assigned a value. It is of type undefined. If a function does not return any value as the result of executing it is assigned to a variable, the variable also has the value of undefined. To check for it, compare using the strict equality (===) operator or typeof which will give the 'undefined' string. Note that you should not be using the abstract equality operator to check, as it will also return true if the value is null.

var foo;
console.log(foo); // undefined
console.log(foo === undefined); // true
console.log(typeof foo === 'undefined'); // true

console.log(foo == null); // true. Wrong, don't use this to check!

function bar() {}
var baz = bar();
console.log(baz); // undefined

A variable that is null will have been explicitly assigned to the null value. It represents no value and is different from undefined in the sense that it has been explicitly assigned. To check for null, simply compare using the strict equality operator. Note that like the above, you should not be using the abstract equality operator (==) to check, as it will also return true if the value is undefined.

var foo = null;
console.log(foo === null); // true
console.log(typeof foo === 'object'); // true

console.log(foo == undefined); // true. Wrong, don't use this to check!

As a personal habit, I never leave my variables undeclared or unassigned. I will explicitly assign null to them after declaring if I don't intend to use it yet. If you use a linter in your workflow, it will usually also be able to check that you are not referencing undeclared variables.

References
https://stackoverflow.com/questions/15985875/effect-of-declared-and-undeclared-variables
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined
What is a closure, and how/why would you use one?
A closure is the combination of a function and the lexical environment within which that function was declared. The word "lexical" refers to the fact that lexical scoping uses the location where a variable is declared within the source code to determine where that variable is available. Closures are functions that have access to the outer (enclosing) function's variables—scope chain even after the outer function has returned.

Why would you use one?

Data privacy / emulating private methods with closures. Commonly used in the module pattern.
Partial applications or currying.
References
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures
https://medium.com/javascript-scene/master-the-javascript-interview-what-is-a-closure-b2f0d2152b36
Can you describe the main difference between a .forEach loop and a .map() loop and why you would pick one versus the other?
To understand the differences between the two, let's look at what each function does.

forEach

Iterates through the elements in an array.
Executes a callback for each element.
Does not return a value.
const a = [1, 2, 3];
const doubled = a.forEach((num, index) => {
  // Do something with num and/or index.
});

// doubled = undefined

map

Iterates through the elements in an array.
"Maps" each element to a new element by calling the function on each element, creating a new array as a result.
const a = [1, 2, 3];
const doubled = a.map((num) => {
  return num * 2;
});

// doubled = [2, 4, 6]

The main difference between .forEach and .map() is that .map() returns a new array. If you need the result, but do not wish to mutate the original array, .map() is the clear choice. If you simply need to iterate over an array, forEach is a fine choice.

References
https://codeburst.io/javascript-map-vs-foreach-f38111822c0f?gi=c9bc30cbec28
What's a typical use case for anonymous functions?
They can be used in IIFEs to encapsulate some code within a local scope so that variables declared in it do not leak to the global scope.

(function () {
  // Some code here.
})();

As a callback that is used once and does not need to be used anywhere else. The code will seem more self-contained and readable when handlers are defined right inside the code calling them, rather than having to search elsewhere to find the function body.

setTimeout(function () {
  console.log('Hello world!');
}, 1000);

Arguments to functional programming constructs or Lodash (similar to callbacks).

const arr = [1, 2, 3];
const double = arr.map(function (el) {
  return el * 2;
});
console.log(double); // [2, 4, 6]

References
https://www.quora.com/What-is-a-typical-usecase-for-anonymous-functions
https://stackoverflow.com/questions/10273185/what-are-the-benefits-to-using-anonymous-functions-instead-of-named-functions-fo
How do you organize your code? (module pattern, classical inheritance?)
In the past, I've used Backbone for my models which encourages a more OOP approach, creating Backbone models and attaching methods to them.

The module pattern is still great, but these days, I use React/Redux which utilize a single-directional data flow based on Flux architecture. I would represent my app's models using plain objects and write utility pure functions to manipulate these objects. State is manipulated using actions and reducers like in any other Redux application.

I avoid using classical inheritance where possible. When and if I do, I stick to these rules.

What's the difference between host objects and native objects?
Native objects are objects that are part of the JavaScript language defined by the ECMAScript specification, such as String, Math, RegExp, Object, Function, etc.

Host objects are provided by the runtime environment (browser or Node), such as window, XMLHTTPRequest, etc.

References
https://stackoverflow.com/questions/7614317/what-is-the-difference-between-native-objects-and-host-objects
Difference between: function Person(){}, var person = Person(), and var person = new Person()?
This question is pretty vague. My best guess at its intention is that it is asking about constructors in JavaScript. Technically speaking, function Person(){} is just a normal function declaration. The convention is to use PascalCase for functions that are intended to be used as constructors.

var person = Person() invokes the Person as a function, and not as a constructor. Invoking as such is a common mistake if the function is intended to be used as a constructor. Typically, the constructor does not return anything, hence invoking the constructor like a normal function will return undefined and that gets assigned to the variable intended as the instance.

var person = new Person() creates an instance of the Person object using the new operator, which inherits from Person.prototype. An alternative would be to use Object.create, such as: Object.create(Person.prototype).

function Person(name) {
  this.name = name;
}

var person = Person('John');
console.log(person); // undefined
console.log(person.name); // Uncaught TypeError: Cannot read property 'name' of undefined

var person = new Person('John');
console.log(person); // Person { name: "John" }
console.log(person.name); // "john"

References
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new
What's the difference between .call and .apply?
Both .call and .apply are used to invoke functions and the first parameter will be used as the value of this within the function. However, .call takes in comma-separated arguments as the next arguments while .apply takes in an array of arguments as the next argument. An easy way to remember this is C for call and comma-separated and A for apply and an array of arguments.

function add(a, b) {
  return a + b;
}

console.log(add.call(null, 1, 2)); // 3
console.log(add.apply(null, [1, 2])); // 3

Explain Function.prototype.bind.
Taken word-for-word from MDN:

The bind() method creates a new function that, when called, has its this keyword set to the provided value, with a given sequence of arguments preceding any provided when the new function is called.

In my experience, it is most useful for binding the value of this in methods of classes that you want to pass into other functions. This is frequently done in React components.

References
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind
When would you use document.write()?
document.write() writes a string of text to a document stream opened by document.open(). When document.write() is executed after the page has loaded, it will call document.open which clears the whole document (<head> and <body> removed!) and replaces the contents with the given parameter value. Hence it is usually considered dangerous and prone to misuse.

There are some answers online that explain document.write() is being used in analytics code or when you want to include styles that should only work if JavaScript is enabled. It is even being used in HTML5 boilerplate to load scripts in parallel and preserve execution order! However, I suspect those reasons might be outdated and in the modern day, they can be achieved without using document.write(). Please do correct me if I'm wrong about this.

References
https://www.quirksmode.org/blog/archives/2005/06/three_javascrip_1.html
https://github.com/h5bp/html5-boilerplate/wiki/#documentwrite-script-tag
What's the difference between feature detection, feature inference, and using the UA string?
Feature Detection

Feature detection involves working out whether a browser supports a certain block of code, and running different code depending on whether it does (or doesn't), so that the browser can always provide a working experience rather crashing/erroring in some browsers. For example:

if ('geolocation' in navigator) {
  // Can use navigator.geolocation
} else {
  // Handle lack of feature
}

Modernizr is a great library to handle feature detection.

Feature Inference

Feature inference checks for a feature just like feature detection, but uses another function because it assumes it will also exist, e.g.:

if (document.getElementsByTagName) {
  element = document.getElementById(id);
}

This is not really recommended. Feature detection is more foolproof.

UA String

This is a browser-reported string that allows the network protocol peers to identify the application type, operating system, software vendor or software version of the requesting software user agent. It can be accessed via navigator.userAgent. However, the string is tricky to parse and can be spoofed. For example, Chrome reports both as Chrome and Safari. So to detect Safari you have to check for the Safari string and the absence of the Chrome string. Avoid this method.

References
https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Testing/Feature_detection
https://stackoverflow.com/questions/20104930/whats-the-difference-between-feature-detection-feature-inference-and-using-th
https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Browser_detection_using_the_user_agent
Explain Ajax in as much detail as possible.
Ajax (asynchronous JavaScript and XML) is a set of web development techniques using many web technologies on the client side to create asynchronous web applications. With Ajax, web applications can send data to and retrieve from a server asynchronously (in the background) without interfering with the display and behavior of the existing page. By decoupling the data interchange layer from the presentation layer, Ajax allows for web pages, and by extension web applications, to change content dynamically without the need to reload the entire page. In practice, modern implementations commonly use JSON instead of XML, due to the advantages of JSON being native to JavaScript.

The XMLHttpRequest API is frequently used for the asynchronous communication or these days, the fetch() API.

References
https://en.wikipedia.org/wiki/Ajax_(programming)
https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Network_requests
What are the advantages and disadvantages of using Ajax?
Advantages

Better interactivity. New content from the server can be changed dynamically without the need to reload the entire page.
Reduce connections to the server since scripts and stylesheets only have to be requested once.
State can be maintained on a page. JavaScript variables and DOM state will persist because the main container page was not reloaded.
Basically most of the advantages of an SPA.
Disadvantages

Dynamic webpages are harder to bookmark.
Does not work if JavaScript has been disabled in the browser.
Some webcrawlers do not execute JavaScript and would not see content that has been loaded by JavaScript.
Webpages using Ajax to fetch data will likely have to combine the fetched remote data with client-side templates to update the DOM. For this to happen, JavaScript will have to be parsed and executed on the browser, and low-end mobile devices might struggle with this.
Basically most of the disadvantages of an SPA.
Explain how JSONP works (and how it's not really Ajax).
JSONP (JSON with Padding) is a method commonly used to bypass the cross-domain policies in web browsers because Ajax requests from the current page to a cross-origin domain is not allowed.

JSONP works by making a request to a cross-origin domain via a <script> tag and usually with a callback query parameter, for example: https://example.com?callback=printData. The server will then wrap the data within a function called printData and return it to the client.

<!-- https://mydomain.com -->
<script>
  function printData(data) {
    console.log(`My name is ${data.name}!`);
  }
</script>

<script src="https://example.com?callback=printData"></script>

// File loaded from https://example.com?callback=printData
printData({ name: 'Yang Shun' });

The client has to have the printData function in its global scope and the function will be executed by the client when the response from the cross-origin domain is received.

JSONP can be unsafe and has some security implications. As JSONP is really JavaScript, it can do everything else JavaScript can do, so you need to trust the provider of the JSONP data.

These days, CORS is the recommended approach and JSONP is seen as a hack.

References
https://stackoverflow.com/a/2067584/1751946
Have you ever used JavaScript templating? If so, what libraries have you used?
Yes. Handlebars, Underscore, Lodash, AngularJS, and JSX. I disliked templating in AngularJS because it made heavy use of strings in the directives and typos would go uncaught. JSX is my new favorite as it is closer to JavaScript and there is barely any syntax to learn. Nowadays, you can even use ES2015 template string literals as a quick way for creating templates without relying on third-party code.

const template = `<div>My name is: ${name}</div>`;

However, do be aware of a potential XSS in the above approach as the contents are not escaped for you, unlike in templating libraries.

Explain "hoisting".
Hoisting is a term used to explain the behavior of variable declarations in your code. Variables declared or initialized with the var keyword will have their declaration "moved" up to the top of their module/function-level scope, which we refer to as hoisting. However, only the declaration is hoisted, the assignment (if there is one), will stay where it is.

Note that the declaration is not actually moved - the JavaScript engine parses the declarations during compilation and becomes aware of declarations and their scopes. It is just easier to understand this behavior by visualizing the declarations as being hoisted to the top of their scope. Let's explain with a few examples.

console.log(foo); // undefined
var foo = 1;
console.log(foo); // 1

Function declarations have the body hoisted while the function expressions (written in the form of variable declarations) only has the variable declaration hoisted.

// Function Declaration
console.log(foo); // [Function: foo]
foo(); // 'FOOOOO'
function foo() {
  console.log('FOOOOO');
}
console.log(foo); // [Function: foo]

// Function Expression
console.log(bar); // undefined
bar(); // Uncaught TypeError: bar is not a function
var bar = function () {
  console.log('BARRRR');
};
console.log(bar); // [Function: bar]

Variables declared via let and const are hoisted as well. However, unlike var and function, they are not initialized and accessing them before the declaration will result in a ReferenceError exception. The variable is in a "temporal dead zone" from the start of the block until the declaration is processed.

x; // undefined
y; // Reference error: y is not defined

var x = 'local';
let y = 'local';

References
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#Variable_hoisting
https://stackoverflow.com/questions/31219420/are-variables-declared-with-let-or-const-not-hoisted-in-es6/31222689#31222689
Describe event bubbling.
When an event triggers on a DOM element, it will attempt to handle the event if there is a listener attached, then the event is bubbled up to its parent and the same thing happens. This bubbling occurs up the element's ancestors all the way to the document. Event bubbling is the mechanism behind event delegation.

What's the difference between an "attribute" and a "property"?
Attributes are defined on the HTML markup but properties are defined on the DOM. To illustrate the difference, imagine we have this text field in our HTML: <input type="text" value="Hello">.

const input = document.querySelector('input');
console.log(input.getAttribute('value')); // Hello
console.log(input.value); // Hello

But after you change the value of the text field by adding "World!" to it, this becomes:

console.log(input.getAttribute('value')); // Hello
console.log(input.value); // Hello World!

References
https://stackoverflow.com/questions/6003819/properties-and-attributes-in-html
Why is extending built-in JavaScript objects not a good idea?
Extending a built-in/native JavaScript object means adding properties/functions to its prototype. While this may seem like a good idea at first, it is dangerous in practice. Imagine your code uses a few libraries that both extend the Array.prototype by adding the same contains method, the implementations will overwrite each other and your code will break if the behavior of these two methods is not the same.

The only time you may want to extend a native object is when you want to create a polyfill, essentially providing your own implementation for a method that is part of the JavaScript specification but might not exist in the user's browser due to it being an older browser.

References
https://lucybain.com/blog/2014/js-extending-built-in-objects/
Difference between document load event and document DOMContentLoaded event?
The DOMContentLoaded event is fired when the initial HTML document has been completely loaded and parsed, without waiting for stylesheets, images, and subframes to finish loading.

window's load event is only fired after the DOM and all dependent resources and assets have loaded.

References
https://developer.mozilla.org/en-US/docs/Web/API/Document/DOMContentLoaded_event
https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event
What is the difference between == and ===?
== is the abstract equality operator while === is the strict equality operator. The == operator will compare for equality after doing any necessary type conversions. The === operator will not do type conversion, so if two values are not the same type === will simply return false. When using ==, funky things can happen, such as:

1 == '1'; // true
1 == [1]; // true
1 == true; // true
0 == ''; // true
0 == '0'; // true
0 == false; // true

My advice is never to use the == operator, except for convenience when comparing against null or undefined, where a == null will return true if a is null or undefined.

var a = null;
console.log(a == null); // true
console.log(a == undefined); // true

References
https://stackoverflow.com/questions/359494/which-equals-operator-vs-should-be-used-in-javascript-comparisons
Explain the same-origin policy with regards to JavaScript.
The same-origin policy prevents JavaScript from making requests across domain boundaries. An origin is defined as a combination of URI scheme, hostname, and port number. This policy prevents a malicious script on one page from obtaining access to sensitive data on another web page through that page's Document Object Model.

References
https://en.wikipedia.org/wiki/Same-origin_policy
Make this work:
duplicate([1, 2, 3, 4, 5]); // [1,2,3,4,5,1,2,3,4,5]

function duplicate(arr) {
  return arr.concat(arr);
}

duplicate([1, 2, 3, 4, 5]); // [1,2,3,4,5,1,2,3,4,5]

Or with ES6:

const duplicate = (arr) => [...arr, ...arr];

duplicate([1, 2, 3, 4, 5]); // [1,2,3,4,5,1,2,3,4,5]

Why is it called a Ternary expression, what does the word "Ternary" indicate?
"Ternary" indicates three, and a ternary expression accepts three operands, the test condition, the "then" expression and the "else" expression. Ternary expressions are not specific to JavaScript and I'm not sure why it is even in this list.

References
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator
What is "use strict";? What are the advantages and disadvantages to using it?
'use strict' is a statement used to enable strict mode to entire scripts or individual functions. Strict mode is a way to opt into a restricted variant of JavaScript.

Advantages:

Makes it impossible to accidentally create global variables.
Makes assignments which would otherwise silently fail to throw an exception.
Makes attempts to delete undeletable properties throw an exception (where before the attempt would simply have no effect).
Requires that function parameter names be unique.
this is undefined in the global context.
It catches some common coding bloopers, throwing exceptions.
It disables features that are confusing or poorly thought out.
Disadvantages:

Many missing features that some developers might be used to.
No more access to function.caller and function.arguments.
Concatenation of scripts written in different strict modes might cause issues.
Overall, I think the benefits outweigh the disadvantages, and I never had to rely on the features that strict mode blocks. I would recommend using strict mode.

References
https://2ality.com/2011/10/strict-mode-hatred.html
https://lucybain.com/blog/2014/js-use-strict/
Create a for loop that iterates up to 100 while outputting "fizz" at multiples of 3, "buzz" at multiples of 5 and "fizzbuzz" at multiples of 3 and 5.
Check out this version of FizzBuzz by Paul Irish.

for (let i = 1; i <= 100; i++) {
  let f = i % 3 == 0,
    b = i % 5 == 0;
  console.log(f ? (b ? 'FizzBuzz' : 'Fizz') : b ? 'Buzz' : i);
}

I would not advise you to write the above during interviews though. Just stick with the long but clear approach. For more wacky versions of FizzBuzz, check out the reference link below.

References
https://gist.github.com/jaysonrowe/1592432
Why is it, in general, a good idea to leave the global scope of a website as-is and never touch it?
Every script has access to the global scope, and if everyone uses the global namespace to define their variables, collisions will likely occur. Use the module pattern (IIFEs) to encapsulate your variables within a local namespace.

Why would you use something like the load event? Does this event have disadvantages? Do you know any alternatives, and why would you use those?
The load event fires at the end of the document loading process. At this point, all of the objects in the document are in the DOM, and all the images, scripts, links and sub-frames have finished loading.

The DOM event DOMContentLoaded will fire after the DOM for the page has been constructed, but do not wait for other resources to finish loading. This is preferred in certain cases when you do not need the full page to be loaded before initializing.

References
https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event
Explain what a single page app is and how to make one SEO-friendly.
The below is taken from the awesome Grab Front End Guide, which coincidentally, is written by me!

Web developers these days refer to the products they build as web apps, rather than websites. While there is no strict difference between the two terms, web apps tend to be highly interactive and dynamic, allowing the user to perform actions and receive a response to their action. Traditionally, the browser receives HTML from the server and renders it. When the user navigates to another URL, a full-page refresh is required and the server sends fresh new HTML to the new page. This is called server-side rendering.

However, in modern SPAs, client-side rendering is used instead. The browser loads the initial page from the server, along with the scripts (frameworks, libraries, app code) and stylesheets required for the whole app. When the user navigates to other pages, a page refresh is not triggered. The URL of the page is updated via the HTML5 History API. New data required for the new page, usually in JSON format, is retrieved by the browser via AJAX requests to the server. The SPA then dynamically updates the page with the data via JavaScript, which it has already downloaded in the initial page load. This model is similar to how native mobile apps work.

The benefits:

The app feels more responsive and users do not see the flash between page navigations due to full-page refreshes.
Fewer HTTP requests are made to the server, as the same assets do not have to be downloaded again for each page load.
Clear separation of the concerns between the client and the server; you can easily build new clients for different platforms (e.g. mobile, chatbots, smart watches) without having to modify the server code. You can also modify the technology stack on the client and server independently, as long as the API contract is not broken.
The downsides:

Heavier initial page load due to the loading of framework, app code, and assets required for multiple pages.
There's an additional step to be done on your server which is to configure it to route all requests to a single entry point and allow client-side routing to take over from there.
SPAs are reliant on JavaScript to render content, but not all search engines execute JavaScript during crawling, and they may see empty content on your page. This inadvertently hurts the Search Engine Optimization (SEO) of your app. However, most of the time, when you are building apps, SEO is not the most important factor, as not all the content needs to be indexable by search engines. To overcome this, you can either server-side render your app or use services such as Prerender to "render your javascript in a browser, save the static HTML, and return that to the crawlers".
References
https://github.com/grab/front-end-guide#single-page-apps-spas
https://stackoverflow.com/questions/21862054/single-page-app-advantages-and-disadvantages
https://blog.isquaredsoftware.com/presentations/2016-10-revolution-of-web-dev/
https://www.freecodecamp.org/news/heres-why-client-side-rendering-won-46a349fadb52
What is the extent of your experience with Promises and/or their polyfills?
Possess working knowledge of it. A promise is an object that may produce a single value sometime in the future: either a resolved value or a reason that it's not resolved (e.g., a network error occurred). A promise may be in one of 3 possible states: fulfilled, rejected, or pending. Promise users can attach callbacks to handle the fulfilled value or the reason for rejection.

Some common polyfills are $.deferred, Q and Bluebird but not all of them comply with the specification. ES2015 supports Promises out of the box and polyfills are typically not needed these days.

References
https://medium.com/javascript-scene/master-the-javascript-interview-what-is-a-promise-27fc71e77261
What are the pros and cons of using Promises instead of callbacks?
Pros

Avoid callback hell which can be unreadable.
Makes it easy to write sequential asynchronous code that is readable with .then().
Makes it easy to write parallel asynchronous code with Promise.all().
With promises, these scenarios which are present in callbacks-only coding, will not happen:
Call the callback too early
Call the callback too late (or never)
Call the callback too few or too many times
Fail to pass along any necessary environment/parameters
Swallow any errors/exceptions that may happen
Cons

Slightly more complex code (debatable).
In older browsers where ES2015 is not supported, you need to load a polyfill in order to use it.
References
https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/async%20%26%20performance/ch3.md
What are some of the advantages/disadvantages of writing JavaScript code in a language that compiles to JavaScript?
Some examples of languages that compile to JavaScript include CoffeeScript, Elm, ClojureScript, PureScript, and TypeScript.

Advantages:

Fixes some of the longstanding problems in JavaScript and discourages JavaScript anti-patterns.
Enables you to write shorter code, by providing some syntactic sugar on top of JavaScript, which I think ES5 lacks, but ES2015 is awesome.
Static types are awesome (in the case of TypeScript) for large projects that need to be maintained over time.
Disadvantages:

Require a build/compile process as browsers only run JavaScript and your code will need to be compiled into JavaScript before being served to browsers.
Debugging can be a pain if your source maps do not map nicely to your pre-compiled source.
Most developers are not familiar with these languages and will need to learn it. There's a ramp up cost involved for your team if you use it for your projects.
Smaller community (depends on the language), which means resources, tutorials, libraries, and tooling would be harder to find.
IDE/editor support might be lacking.
These languages will always be behind the latest JavaScript standard.
Developers should be cognizant of what their code is being compiled to — because that is what would actually be running, and that is what matters in the end.
Practically, ES2015 has vastly improved JavaScript and made it much nicer to write. I don't really see the need for CoffeeScript these days.

References
https://softwareengineering.stackexchange.com/questions/72569/what-are-the-pros-and-cons-of-coffeescript
What tools and techniques do you use for debugging JavaScript code?
React and Redux
React Devtools
Redux Devtools
Vue
Vue Devtools
JavaScript
Chrome Devtools
debugger statement
Good old console.log debugging
References
https://raygun.com/learn/javascript-debugging-tips
What language constructions do you use for iterating over object properties and array items?
For objects:

for-in loops - for (var property in obj) { console.log(property); }. However, this will also iterate through its inherited properties, and you will add an obj.hasOwnProperty(property) check before using it.
Object.keys() - Object.keys(obj).forEach(function (property) { ... }). Object.keys() is a static method that will lists all enumerable properties of the object that you pass it.
Object.getOwnPropertyNames() - Object.getOwnPropertyNames(obj).forEach(function (property) { ... }). Object.getOwnPropertyNames() is a static method that will lists all enumerable and non-enumerable properties of the object that you pass it.
For arrays:

for loops - for (var i = 0; i < arr.length; i++). The common pitfall here is that var is in the function scope and not the block scope and most of the time you would want block scoped iterator variable. ES2015 introduces let which has block scope and it is recommended to use that instead. So this becomes: for (let i = 0; i < arr.length; i++).
forEach - arr.forEach(function (el, index) { ... }). This construct can be more convenient at times because you do not have to use the index if all you need is the array elements. There are also the every and some methods which will allow you to terminate the iteration early.
for-of loops - for (let elem of arr) { ... }. ES6 introduces a new loop, the for-of loop, that allows you to loop over objects that conform to the iterable protocol such as String, Array, Map, Set, etc. It combines the advantages of the for loop and the forEach() method. The advantage of the for loop is that you can break from it, and the advantage of forEach() is that it is more concise than the for loop because you don't need a counter variable. With the for-of loop, you get both the ability to break from a loop and a more concise syntax.
Most of the time, I would prefer the .forEach method, but it really depends on what you are trying to do. Before ES6, we used for loops when we needed to prematurely terminate the loop using break. But now with ES6, we can do that with for-of loops. I would use for loops when I need even more flexibility, such as incrementing the iterator more than once per loop.

Also, when using the for-of loop, if you need to access both the index and value of each array element, you can do so with the ES6 Array entries() method and destructuring:

const arr = ['a', 'b', 'c'];

for (let [index, elem] of arr.entries()) {
  console.log(index, ': ', elem);
}

References
https://2ality.com/2015/08/getting-started-es6.html#from-for-to-foreach-to-for-of
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/entries
Explain the difference between mutable and immutable objects.
Immutability is a core principle in functional programming, and has lots to offer to object-oriented programs as well. A mutable object is an object whose state can be modified after it is created. An immutable object is an object whose state cannot be modified after it is created.

What is an example of an immutable object in JavaScript?
In JavaScript, some built-in types (numbers, strings) are immutable, but custom objects are generally mutable.

Some built-in immutable JavaScript objects are Math, Date.

Here are a few ways to add/simulate immutability on plain JavaScript objects.

Object Constant Properties

By combining writable: false and configurable: false, you can essentially create a constant (cannot be changed, redefined or deleted) as an object property, like:

let myObject = {};
Object.defineProperty(myObject, 'number', {
  value: 42,
  writable: false,
  configurable: false,
});
console.log(myObject.number); // 42
myObject.number = 43;
console.log(myObject.number); // 42

Prevent Extensions

If you want to prevent an object from having new properties added to it, but otherwise leave the rest of the object's properties alone, call Object.preventExtensions(...):

var myObject = {
  a: 2,
};

Object.preventExtensions(myObject);

myObject.b = 3;
myObject.b; // undefined

In non-strict mode, the creation of b fails silently. In strict mode, it throws a TypeError.

Seal

Object.seal() creates a "sealed" object, which means it takes an existing object and essentially calls Object.preventExtensions() on it, but also marks all its existing properties as configurable: false.

So, not only can you not add any more properties, but you also cannot reconfigure or delete any existing properties (though you can still modify their values).

Freeze

Object.freeze() creates a frozen object, which means it takes an existing object and essentially calls Object.seal() on it, but it also marks all "data accessor" properties as writable:false, so that their values cannot be changed.

This approach is the highest level of immutability that you can attain for an object itself, as it prevents any changes to the object or to any of its direct properties (though, as mentioned above, the contents of any referenced other objects are unaffected).

var immutable = Object.freeze({});

Freezing an object does not allow new properties to be added to an object and prevents from removing or altering the existing properties. Object.freeze() preserves the enumerability, configurability, writability and the prototype of the object. It returns the passed object and does not create a frozen copy.

What are the pros and cons of immutability?
Pros

Easier change detection - Object equality can be determined in a performant and easy manner through referential equality. This is useful for comparing object differences in React and Redux.
Programs with immutable objects are less complicated to think about, since you don't need to worry about how an object may evolve over time.
Defensive copies are no longer necessary when immutable objects are returning from or passed to functions, since there is no possibility an immutable object will be modified by it.
Easy sharing via references - One copy of an object is just as good as another, so you can cache objects or reuse the same object multiple times.
Thread-safe - Immutable objects can be safely used between threads in a multi-threaded environment since there is no risk of them being modified in other concurrently running threads.
Using libraries like ImmutableJS, objects are modified using structural sharing and less memory is needed for having multiple objects with similar structures.
Cons

Naive implementations of immutable data structures and its operations can result in extremely poor performance because new objects are created each time. It is recommended to use libraries for efficient immutable data structures and operations that leverage on structural sharing.
Allocation (and deallocation) of many small objects rather than modifying existing ones can cause a performance impact. The complexity of either the allocator or the garbage collector usually depends on the number of objects on the heap.
Cyclic data structures such as graphs are difficult to build. If you have two objects which can't be modified after initialization, how can you get them to point to each other?
References
https://stackoverflow.com/questions/1863515/pros-cons-of-immutability-vs-mutability
How can you achieve immutability in your own code?
One way to achieve immutability is to use libraries like immutable.js, mori or immer.

The alternative is to use const declarations combined with the techniques mentioned above for creation. For "mutating" objects, use the spread operator, Object.assign, Array.concat(), etc., to create new objects instead of mutate the original object.

Examples:

// Array Example
const arr = [1, 2, 3];
const newArr = [...arr, 4]; // [1, 2, 3, 4]

// Object Example
const human = Object.freeze({ race: 'human' });
const john = { ...human, name: 'John' }; // {race: "human", name: "John"}
const alienJohn = { ...john, race: 'alien' }; // {race: "alien", name: "John"}

References
https://stackoverflow.com/questions/1863515/pros-cons-of-immutability-vs-mutability
https://www.sitepoint.com/immutability-javascript/
https://wecodetheweb.com/2016/02/12/immutable-javascript-using-es6-and-beyond/
Explain the difference between synchronous and asynchronous functions.
Synchronous functions are blocking while asynchronous functions are not. In synchronous functions, statements complete before the next statement is run. In this case, the program is evaluated exactly in order of the statements and execution of the program is paused if one of the statements take a very long time.

Asynchronous functions usually accept a callback as a parameter and execution continue on the next line immediately after the asynchronous function is invoked. The callback is only invoked when the asynchronous operation is complete and the call stack is empty. Heavy duty operations such as loading data from a web server or querying a database should be done asynchronously so that the main thread can continue executing other operations instead of blocking until that long operation to complete (in the case of browsers, the UI will freeze).

What is event loop? What is the difference between call stack and task queue?
The event loop is a single-threaded loop that monitors the call stack and checks if there is any work to be done in the task queue. If the call stack is empty and there are callback functions in the task queue, a function is dequeued and pushed onto the call stack to be executed.

If you haven't already checked out Philip Robert's talk on the Event Loop, you should. It is one of the most viewed videos on JavaScript.

References
https://2014.jsconf.eu/speakers/philip-roberts-what-the-heck-is-the-event-loop-anyway.html
Explain the differences on the usage of foo between function foo() {} and var foo = function() {}
The former is a function declaration while the latter is a function expression. The key difference is that function declarations have its body hoisted but the bodies of function expressions are not (they have the same hoisting behavior as variables). For more explanation on hoisting, refer to the question above on hoisting. If you try to invoke a function expression before it is defined, you will get an Uncaught TypeError: XXX is not a function error.

Function Declaration

foo(); // 'FOOOOO'
function foo() {
  console.log('FOOOOO');
}

Function Expression

foo(); // Uncaught TypeError: foo is not a function
var foo = function () {
  console.log('FOOOOO');
};

References
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function
What are the differences between variables created using let, var or const?
Variables declared using the var keyword are scoped to the function in which they are created, or if created outside of any function, to the global object. let and const are block scoped, meaning they are only accessible within the nearest set of curly braces (function, if-else block, or for-loop).

function foo() {
  // All variables are accessible within functions.
  var bar = 'bar';
  let baz = 'baz';
  const qux = 'qux';

  console.log(bar); // bar
  console.log(baz); // baz
  console.log(qux); // qux
}

console.log(bar); // ReferenceError: bar is not defined
console.log(baz); // ReferenceError: baz is not defined
console.log(qux); // ReferenceError: qux is not defined

if (true) {
  var bar = 'bar';
  let baz = 'baz';
  const qux = 'qux';
}

// var declared variables are accessible anywhere in the function scope.
console.log(bar); // bar
// let and const defined variables are not accessible outside of the block they were defined in.
console.log(baz); // ReferenceError: baz is not defined
console.log(qux); // ReferenceError: qux is not defined


var allows variables to be hoisted, meaning they can be referenced in code before they are declared. let and const will not allow this, instead throwing an error.

console.log(foo); // undefined

var foo = 'foo';

console.log(baz); // ReferenceError: can't access lexical declaration 'baz' before initialization

let baz = 'baz';

console.log(bar); // ReferenceError: can't access lexical declaration 'bar' before initialization

const bar = 'bar';


Redeclaring a variable with var will not throw an error, but let and const will.

var foo = 'foo';
var foo = 'bar';
console.log(foo); // "bar"

let baz = 'baz';
let baz = 'qux'; // Uncaught SyntaxError: Identifier 'baz' has already been declared

let and const differ in that let allows reassigning the variable's value while const does not.

// This is fine.
let foo = 'foo';
foo = 'bar';

// This causes an exception.
const baz = 'baz';
baz = 'qux';

References
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const
What are the differences between ES6 class and ES5 function constructors?
Let's first look at an example of each:

// ES5 Function Constructor
function Person(name) {
  this.name = name;
}

// ES6 Class
class Person {
  constructor(name) {
    this.name = name;
  }
}

For simple constructors, they look pretty similar.

The main difference in the constructor comes when using inheritance. If we want to create a Student class that subclasses Person and add a studentId field, this is what we have to do in addition to the above.

// ES5 Function Constructor
function Student(name, studentId) {
  // Call constructor of superclass to initialize superclass-derived members.
  Person.call(this, name);

  // Initialize subclass's own members.
  this.studentId = studentId;
}

Student.prototype = Object.create(Person.prototype);
Student.prototype.constructor = Student;

// ES6 Class
class Student extends Person {
  constructor(name, studentId) {
    super(name);
    this.studentId = studentId;
  }
}

It's much more verbose to use inheritance in ES5 and the ES6 version is easier to understand and remember.

References
https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Advanced_JavaScript_objects/Classes_in_JavaScript
https://eli.thegreenplace.net/2013/10/22/classical-inheritance-in-javascript-es5
Can you offer a use case for the new arrow => function syntax? How does this new syntax differ from other functions?
One obvious benefit of arrow functions is to simplify the syntax needed to create functions, without a need for the function keyword. The this within arrow functions is also bound to the enclosing scope which is different compared to regular functions where the this is determined by the object calling it. Lexically-scoped this is useful when invoking callbacks especially in React components.

What advantage is there for using the arrow syntax for a method in a constructor?
The main advantage of using an arrow function as a method inside a constructor is that the value of this gets set at the time of the function creation and can't change after that. So, when the constructor is used to create a new object, this will always refer to that object. For example, let's say we have a Person constructor that takes a first name as an argument has two methods to console.log that name, one as a regular function and one as an arrow function:

const Person = function (firstName) {
  this.firstName = firstName;
  this.sayName1 = function () {
    console.log(this.firstName);
  };
  this.sayName2 = () => {
    console.log(this.firstName);
  };
};

const john = new Person('John');
const dave = new Person('Dave');

john.sayName1(); // John
john.sayName2(); // John

// The regular function can have its 'this' value changed, but the arrow function cannot
john.sayName1.call(dave); // Dave (because "this" is now the dave object)
john.sayName2.call(dave); // John

john.sayName1.apply(dave); // Dave (because 'this' is now the dave object)
john.sayName2.apply(dave); // John

john.sayName1.bind(dave)(); // Dave (because 'this' is now the dave object)
john.sayName2.bind(dave)(); // John

var sayNameFromWindow1 = john.sayName1;
sayNameFromWindow1(); // undefined (because 'this' is now the window object)

var sayNameFromWindow2 = john.sayName2;
sayNameFromWindow2(); // John

The main takeaway here is that this can be changed for a normal function, but the context always stays the same for an arrow function. So even if you are passing around your arrow function to different parts of your application, you wouldn't have to worry about the context changing.

This can be particularly helpful in React class components. If you define a class method for something such as a click handler using a normal function, and then you pass that click handler down into a child component as a prop, you will need to also bind this in the constructor of the parent component. If you instead use an arrow function, there is no need to also bind "this", as the method will automatically get its "this" value from its enclosing lexical context. (See this article for an excellent demonstration and sample code: https://machnicki.medium.com/handle-events-in-react-with-arrow-functions-ede88184bbb)

References
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions
https://machnicki.medium.com/handle-events-in-react-with-arrow-functions-ede88184bbb
What is the definition of a higher-order function?
A higher-order function is any function that takes one or more functions as arguments, which it uses to operate on some data, and/or returns a function as a result. Higher-order functions are meant to abstract some operation that is performed repeatedly. The classic example of this is map, which takes an array and a function as arguments. map then uses this function to transform each item in the array, returning a new array with the transformed data. Other popular examples in JavaScript are forEach, filter, and reduce. A higher-order function doesn't just need to be manipulating arrays as there are many use cases for returning a function from another function. Function.prototype.bind is one such example in JavaScript.

Map

Let's say we have an array of names which we need to transform each string to uppercase.

const names = ['irish', 'daisy', 'anna'];

The imperative way will be as such:

const transformNamesToUppercase = function (names) {
  const results = [];
  for (let i = 0; i < names.length; i++) {
    results.push(names[i].toUpperCase());
  }
  return results;
};
transformNamesToUppercase(names); // ['IRISH', 'DAISY', 'ANNA']

Use .map(transformerFn) makes the code shorter and more declarative.

const transformNamesToUppercase = function (names) {
  return names.map((name) => name.toUpperCase());
};
transformNamesToUppercase(names); // ['IRISH', 'DAISY', 'ANNA']

References
https://medium.com/javascript-scene/higher-order-functions-composing-software-5365cf2cbe99
https://hackernoon.com/effective-functional-javascript-first-class-and-higher-order-functions-713fde8df50a
https://eloquentjavascript.net/05_higher_order.html
Can you give an example for destructuring an object or an array?
Destructuring is an expression available in ES6 which enables a succinct and convenient way to extract values of Objects or Arrays and place them into distinct variables.

Array destructuring

// Variable assignment.
const foo = ['one', 'two', 'three'];

const [one, two, three] = foo;
console.log(one); // "one"
console.log(two); // "two"
console.log(three); // "three"

// Swapping variables
let a = 1;
let b = 3;

[a, b] = [b, a];
console.log(a); // 3
console.log(b); // 1

Object destructuring

// Variable assignment.
const o = { p: 42, q: true };
const { p, q } = o;

console.log(p); // 42
console.log(q); // true

References
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring
https://ponyfoo.com/articles/es6-destructuring-in-depth
ES6 Template Literals offer a lot of flexibility in generating strings, can you give an example?
Template literals help make it simple to do string interpolation, or to include variables in a string. Before ES2015, it was common to do something like this:

var person = { name: 'Tyler', age: 28 };
console.log(
  'Hi, my name is ' + person.name + ' and I am ' + person.age + ' years old!',
);
// 'Hi, my name is Tyler and I am 28 years old!'

With template literals, you can now create that same output like this instead:

const person = { name: 'Tyler', age: 28 };
console.log(`Hi, my name is ${person.name} and I am ${person.age} years old!`);
// 'Hi, my name is Tyler and I am 28 years old!'

Note that you use backticks, not quotes, to indicate that you are using a template literal and that you can insert expressions inside the ${} placeholders.

A second helpful use case is in creating multi-line strings. Before ES2015, you could create a multi-line string like this:

console.log('This is line one.\nThis is line two.');
// This is line one.
// This is line two.

Or if you wanted to break it up into multiple lines in your code so you didn't have to scroll to the right in your text editor to read a long string, you could also write it like this:

console.log('This is line one.\n' + 'This is line two.');
// This is line one.
// This is line two.

Template literals, however, preserve whatever spacing you add to them. For example, to create that same multi-line output that we created above, you can simply do:

console.log(`This is line one.
This is line two.`);
// This is line one.
// This is line two.

Another use case of template literals would be to use as a substitute for templating libraries for simple variable interpolations:

const person = { name: 'Tyler', age: 28 };
document.body.innerHTML = `
  <div>
    <p>Name: ${person.name}</p>
    <p>Age: ${person.age}</p>
  </div>
`;

Note that your code may be susceptible to XSS by using .innerHTML. Sanitize your data before displaying it if it came from a user!

References
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals
Can you give an example of a curry function and why this syntax offers an advantage?
Currying is a pattern where a function with more than one parameter is broken into multiple functions that, when called in series, will accumulate all of the required parameters one at a time. This technique can be useful for making code written in a functional style easier to read and compose. It's important to note that for a function to be curried, it needs to start out as one function, then broken out into a sequence of functions that each accepts one parameter.

function curry(fn) {
  if (fn.length === 0) {
    return fn;
  }

  function _curried(depth, args) {
    return function (newArgument) {
      if (depth - 1 === 0) {
        return fn(...args, newArgument);
      }
      return _curried(depth - 1, [...args, newArgument]);
    };
  }

  return _curried(fn.length, []);
}

function add(a, b) {
  return a + b;
}

var curriedAdd = curry(add);
var addFive = curriedAdd(5);

var result = [0, 1, 2, 3, 4, 5].map(addFive); // [5, 6, 7, 8, 9, 10]

References
https://hackernoon.com/currying-in-js-d9ddc64f162e
What are the benefits of using spread syntax and how is it different from rest syntax?
ES6's spread syntax is very useful when coding in a functional paradigm as we can easily create copies of arrays or objects without resorting to Object.create, slice, or a library function. This language feature is used often in Redux and RxJS projects.

function putDookieInAnyArray(arr) {
  return [...arr, 'dookie'];
}

const result = putDookieInAnyArray(['I', 'really', "don't", 'like']); // ["I", "really", "don't", "like", "dookie"]

const person = {
  name: 'Todd',
  age: 29,
};

const copyOfTodd = { ...person };


ES6's rest syntax offers a shorthand for including an arbitrary number of arguments to be passed to a function. It is like an inverse of the spread syntax, taking data and stuffing it into an array rather than unpacking an array of data, and it works in function arguments, as well as in array and object destructuring assignments.

function addFiveToABunchOfNumbers(...numbers) {
  return numbers.map((x) => x + 5);
}

const result = addFiveToABunchOfNumbers(4, 5, 6, 7, 8, 9, 10); // [9, 10, 11, 12, 13, 14, 15]

const [a, b, ...rest] = [1, 2, 3, 4]; // a: 1, b: 2, rest: [3, 4]

const { e, f, ...others } = {
  e: 1,
  f: 2,
  g: 3,
  h: 4,
}; // e: 1, f: 2, others: { g: 3, h: 4 }

References
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring
How can you share code between files?
This depends on the JavaScript environment.

On the client (browser environment), as long as the variables/functions are declared in the global scope (window), all scripts can refer to them. Alternatively, adopt the Asynchronous Module Definition (AMD) via RequireJS for a more modular approach.

On the server (Node.js), the common way has been to use CommonJS. Each file is treated as a module and it can export variables and functions by attaching them to the module.exports object.

ES2015 defines a module syntax which aims to replace both AMD and CommonJS. This will eventually be supported in both browser and Node environments.

References
https://requirejs.org/docs/whyamd.html
https://nodejs.org/docs/latest/api/modules.html
https://2ality.com/2014/09/es6-modules-final.html
Why might you want to create static class members?
Static class members (properties/methods) are not tied to a specific instance of a class and have the same value regardless of which instance is referring to it. Static properties are typically configuration variables and static methods are usually pure utility functions which do not depend on the state of the instance.

References
https://stackoverflow.com/questions/21155438/when-to-use-static-variables-methods-and-when-to-use-instance-variables-methods