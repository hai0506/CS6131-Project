---
jupyter:
  kernelspec:
    display_name: Python 3.9.12 (\'base\')
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.9.12
  nbformat: 4
  nbformat_minor: 4
  vscode:
    interpreter:
      hash: 9fa3df5f1ded1049c7d58d39f17ce042f0f0a992cc742838a9127d917b5cd27f
---

::: {.cell .markdown}
```{=html}
<P>
```
`<img src="https://i.ibb.co/gyNf19D/nhslogo.png" alt="nhslogo" border="0" width="100" align="right">`{=html}`<font size="6">`{=html}`<b>`{=html}
CS6131 Database Design`</b>`{=html} `</font>`{=html}
:::

::: {.cell .markdown}
# Project Final Report Submission
:::

::: {.cell .markdown}
### By Trinh Hoang Hai
:::

::: {.cell .markdown}
### Submission Instructions
:::

::: {.cell .markdown}
```{=html}
<div class="alert alert-block alert-info">

* You will need to submit the following files in your final project submission:
    * Your Jupyter Notebook report. Name the report `ProjectFinalReport<YourName>.ipynb`.
    * All relevant image files to be displayed in this report (make sure you use relative file referencing and the image will display in another computer).
    * Attached each file one by one and upload on Coursemology.
* Please print a copy of the final report to OneNote Individual Notebook space > Project. Double check on the image resolution. If the resolution is poor, please copy and paste the ORIGINAL clear image into the OneNote page (paste at the side of the printed image).

* Any submission that fails to comply to the above instructions will result in upto 5% penalty.

* You may wish to refer to the following reference to help organize and "beautify" your final report here. <br>
https://thecodingbot.com/markdown-in-jupyter-ipython-notebook-cheatsheet/
</div>
```
:::

::: {.cell .markdown}
### Section A: Overview & Business Rules {#section-a-overview--business-rules}
:::

::: {.cell .markdown}
#### Overview
:::

::: {.cell .markdown}
```{=html}
<div class="alert alert-block alert-warning">
Complete your writeup of the project overview here.
</div>
```
:::

::: {.cell .markdown}
Online shopping is a popular alternative to visiting physical retailers.
Customers can browse, buy and receive products wherever they want. One
common type of online vendors are clothing stores. Unlike physical
stores where space is a constraint, online stores allow for all
available items to be displayed to the customer. Customers can also
quickly find the product they have in mind using the search function of
the store website.

To easily manage customer orders, the database should be able to relate
customers to the products they bought, which is a fitting job for an
RDBMS system. An RDBMS system also allows for fast queries of products,
search filtering and grouping of products into multiple categories,
giving the customer a better shopping experience.
:::

::: {.cell .markdown}
#### Business Rules
:::

::: {.cell .markdown}
```{=html}
<div class="alert alert-block alert-warning">
Include your updated business rules writeup here. Any changes from previous submission should be highlighted.
You may consider using HTML editor for easy editing e.g. <a href="https://onlinehtmleditor.dev/">https://onlinehtmleditor.dev/</a>
</div>
```
:::

::: {.cell .markdown}
Each **customer** in the database can be identified by a unique customer
ID. They are required to provide an email, phone number and address for
delivery purposes. Customers also have login details consisting of a
username and a password, as well as a name and date of birth if they
choose to sign up for an account.

To draw customers, the store sometimes gives out exclusive
**discounts**, each with a code, start date, end date, and amount of
discount.A customer cannot have two discounts with the same code, but
multiple customerscan have the same discount code. Not all have
discounts, but all discounts must have a customer as the owner.

Customers can write **feedbacks**, which are messages of all kinds for
the store. Feedbacks have unique IDs, category of feedback (complaint,
questions regarding an item, request refund, etc.) and the contents.

**Products** are items sold in the store. Each product has a unique
product ID, a name, number of items in stock, type (shirts, pants, etc),
size, price, colors, categories it belongs to (men, women,
accessories)`<span style="background-color:#ffff00">`{=html} and the
link to its photo.`</span>`{=html} A product can be of multiple colors
and belong to multiple categories. Note that similar products with
different sizes are considered 2 separate products. For example, a
\"Baseball Long Sleeve - B&W\" of size S is a separate product from a
\"Baseball Long Sleeve - B&W\" of size L. Each would have their own
unique IDs and may have different prices.

Occasionally, there may be **sale** events where a (non-zero) number of
products have their prices lowered. Sales are identified by a unique
sale ID, start date, end date,
`<span style="background-color:#ffff00">`{=html}description`</span>`{=html},
and amount of discount.
`<span style="background-color:#ffff00">`{=html}A product can be on
multiple sales, and a sale can apply for multiple
products.`</span>`{=html}

Customers can favourite products, adding them to a wishlist. They can
also write reviews on products. When reviewing, the user give an overall
rating and a comment on the product. The time when the review was posted
is also recorded.

**Designers** make the products. Each designer has a unique designer ID,
a name, description and a link to their website (to be displayed on
their information page). Designers make multiple products, and a product
is made by only one designer. Only designers whose products are sold in
the store are saved in the database. The date at which a product is made
and given to the store is stored.

**Orders** are practically the shopping carts of the online store. Each
order has a unique ID and a total price. Products can be added to orders
with a specified quantity, i.e how many Blue Plaid Shirts are to be put
in the cart. `<span style="background-color:#ffff00">`{=html}When an
order is made by a customer, it is shipped with a shipping cost and
shipping status for tracking. The date at which the order is made is
recorded.`</span>`{=html} The total price is derived from all the items
bought and the delivery fee.
:::

::: {.cell .markdown}
### Section B: ER Model
:::

::: {.cell .markdown}
```{=html}
<div class="alert alert-block alert-warning">
Attached the image of your FINAL ER Model here.
</div>
```
:::

::: {.cell .markdown}
`<img src="report/ER.png">`{=html}
:::

::: {.cell .markdown}
### Section C: Relational Model
:::

::: {.cell .markdown}
```{=html}
<div class="alert alert-block alert-warning">
Attached the image of your FINAL Relational Model here.
</div>
```
:::

::: {.cell .markdown}
`<img src="report/Schema.png">`{=html}
:::

::: {.cell .markdown}
```{=html}
<div class="alert alert-block alert-warning">
Justify your mapping strategy from ER to relational, particularly if the approach deviates from the norm, or you have inheritance in your ER model (i.e. which strategy is adopted for inheritance mapping and why).
</div>
```
:::

::: {.cell .markdown}
N:1 relationships are mapped by adding the primary key of a relation as
foreign key of the other to avoid creating more tables.
:::

::: {.cell .markdown}
```{=html}
<div class="alert alert-block alert-warning">
If the relational schema mapped from the ER is not in 3NF, propose relevant normalization to make all relations in 3NF. You may leave this part blank if no further normalization is required.
</div>
```
:::

::: {.cell .markdown}
Proposed normalization, if any
:::

::: {.cell .markdown}
### Section D: DDL Schema
:::

::: {.cell .markdown}
```{=html}
<div class="alert alert-block alert-warning">
Fill in the relevant code required to create the relations from your database. <br>
Your code should be end to end (i.e. I should be able to execute on my computer without much problem).
</div>
```
:::

::: {.cell .code execution_count="116"}
``` python
%load_ext sql
```

::: {.output .stream .stdout}
    The sql extension is already loaded. To reload it, use:
      %reload_ext sql
:::
:::

::: {.cell .code execution_count="117"}
``` python
%sql mysql+pymysql://root:admin@localhost/  --make sure user is root and password is admin
```
:::

::: {.cell .code execution_count="118"}
``` python
%%sql
DROP DATABASE IF EXISTS STORE;
CREATE DATABASE STORE;
USE STORE;

create table customer (
  cid int NOT NULL AUTO_INCREMENT,
  email varchar(50),
  phoneNo varchar(25), 
  address varchar(255),
  username varchar(50),
  password varchar(200),
  name varchar(50),
  dateOfBirth date,
  primary key (cid)
);

create table discount (
  code varchar(10),
  cid int,
  amount int,
  startDate date,
  endDate date,
  primary key (code,cid),
  foreign key (cid) references customer(cid) on delete cascade on update cascade
);

create table feedback (
  feedbackid int NOT NULL AUTO_INCREMENT,
  cid int,
  category varchar(50),
  content varchar(250),
  primary key (feedbackid),
  foreign key (cid) references customer(cid) on delete cascade on update cascade
);

create table sale (
  saleid int NOT NULL AUTO_INCREMENT,
  amount int,
  startDate date,
  endDate date,
  description varchar(50),
  primary key (saleid)
);

create table designer (
  designerid int NOT NULL AUTO_INCREMENT,
  name varchar(50),
  bio TEXT, # desc is a reserved word
  website varchar(100),
  primary key (designerid)
);

create table product (
  pid int NOT NULL AUTO_INCREMENT,
  name varchar(50),
  stock int,
  type varchar(20),
  size varchar(4),
  price float,
  designerid int,
  addDate date,
  image varchar(255),
  primary key (pid),
  foreign key (designerid) references designer(designerid) on delete cascade on update cascade
);

create table onsale (
  saleid int,
  pid int,
  primary key (pid,saleid),
  foreign key (pid) references product(pid) on delete cascade on update cascade,
  foreign key (saleid) references sale(saleid) on delete cascade on update cascade
);

create table review (
  pid int,
  cid int,
  rating int,
  comment varchar(250),
  date date,
  primary key (pid, cid),
  foreign key (pid) references product(pid) on delete cascade on update cascade,
  foreign key (cid) references customer(cid) on delete cascade on update cascade
);

create table color (
  pid int,
  color varchar(10),
  primary key (pid, color),
  foreign key (pid) references product(pid) on delete cascade on update cascade
);

create table category (
  pid int,
  category varchar(20),
  primary key (pid, category),
  foreign key (pid) references product(pid) on delete cascade on update cascade
);

create table cart ( # order is a reserved word
  cartid int NOT NULL AUTO_INCREMENT,
  totalPrice float null default 0.0,
  cid int,
  date date,
  shipCost float,
  status varchar(50),
  primary key (cartid),
  foreign key (cid) references customer (cid) on delete cascade on update cascade
);

create table favourite (
  pid int,
  cid int,
  primary key(pid,cid),
  foreign key (pid) references product(pid) on delete cascade on update cascade,
  foreign key (cid) references customer(cid) on delete cascade on update cascade
);

create table addedto (
  pid int,
  cartid int,
  quantity int,
  primary key(pid,cartid),
  foreign key (pid) references product(pid) on delete cascade on update cascade,
  foreign key (cartid) references cart(cartid) on delete cascade on update cascade
);
```

::: {.output .stream .stdout}
     * mysql+pymysql://root:***@localhost/
    13 rows affected.
    1 rows affected.
    0 rows affected.
    0 rows affected.
    0 rows affected.
    0 rows affected.
    0 rows affected.
    0 rows affected.
    0 rows affected.
    0 rows affected.
    0 rows affected.
    0 rows affected.
    0 rows affected.
    0 rows affected.
    0 rows affected.
    0 rows affected.
:::

::: {.output .execute_result execution_count="118"}
    []
:::
:::

::: {.cell .markdown}
### Section E: Data Population Script
:::

::: {.cell .markdown}
```{=html}
<div class="alert alert-block alert-warning">
Fill in relevant code to populate data into your database. It is sufficient to have 20-50 records per table (some may have more, some less). They should be logically related and realistic. Please do not overpopulate data.
    
Note that you should use INSERT commands. If you are are using other means to populate your database, please ensure I can run the scripts easily. 
</div>
```
:::

::: {.cell .code execution_count="119"}
``` python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="store"
)

mycursor = mydb.cursor()
f = open("inserts.txt", "r")
for x in f: 
  mycursor.execute(x[:len(x)-2])
f.close()
mydb.commit()
mycursor.close()
```

::: {.output .execute_result execution_count="119"}
    True
:::
:::

::: {.cell .markdown}
```{=html}
<div class="alert alert-block alert-warning">
Add in relevant select statements to show that your data is populated correctly FOR EACH relation, one cell each relation.
</div>
```
:::

::: {.cell .code execution_count="120"}
``` python
%%sql
select * from customer
```

::: {.output .stream .stdout}
     * mysql+pymysql://root:***@localhost/
    30 rows affected.
:::

::: {.output .execute_result execution_count="120"}
```{=html}
<table>
    <tr>
        <th>cid</th>
        <th>email</th>
        <th>phoneNo</th>
        <th>address</th>
        <th>username</th>
        <th>password</th>
        <th>name</th>
        <th>dateOfBirth</th>
    </tr>
    <tr>
        <td>1</td>
        <td>EllieCremin@gmail.com</td>
        <td>(504) 408-5896 x7526</td>
        <td>Suite 460 72502 Murray Throughway, Ionafort, SD 87176</td>
        <td>elliecremin</td>
        <td>pbkdf2:sha256:260000$S2kptIOviFB0dm95$ab76512ea4e7f717ad823432105714b48472693a5b602c698c9622a834f9fa0d</td>
        <td>Ellie Cremin</td>
        <td>1965-02-14</td>
    </tr>
    <tr>
        <td>2</td>
        <td>CatherinaMoen@gmail.com</td>
        <td>(828) 618-6911</td>
        <td>Apt. 490 656 O&#x27;Reilly Haven, North Kathaleen, RI 23054</td>
        <td>catherinamoen</td>
        <td>pbkdf2:sha256:260000$dnHwoOl12sb8d8r6$856fc023a66d3169bd0e7738e23d83da3ae8679c6218075a7a3fa1e440691a99</td>
        <td>Catherina Moen</td>
        <td>1971-09-14</td>
    </tr>
    <tr>
        <td>3</td>
        <td>HansWolf@gmail.com</td>
        <td>(256) 209-9024 x9933</td>
        <td>Suite 103 1504 Bartell Courts, New Delfinamouth, LA 11280</td>
        <td>hanswolf</td>
        <td>pbkdf2:sha256:260000$trAST5JMOhrXQ41M$afddbca6467885766992452d7e37bca790aa3e293141cad39cb522b84632400b</td>
        <td>Hans Wolf</td>
        <td>1987-10-12</td>
    </tr>
    <tr>
        <td>4</td>
        <td>ElnoraFerry@gmail.com</td>
        <td>(715) 305-2593</td>
        <td>Suite 130 310 Conn Lodge, Wehnermouth, LA 66636</td>
        <td>elnoraferry</td>
        <td>pbkdf2:sha256:260000$4LlDzhwTuIOhdvLy$1b3a97bc2ffe565a4ae22577544e33619fd7f5f4fbe9a247e66e11230b369c1d</td>
        <td>Elnora Ferry</td>
        <td>1967-08-17</td>
    </tr>
    <tr>
        <td>5</td>
        <td>PatsyHauck@gmail.com</td>
        <td>(562) 616-6787 x3247</td>
        <td>Suite 286 455 Senger Garden, Greenburgh, SD 83527</td>
        <td>patsyhauck</td>
        <td>pbkdf2:sha256:260000$JYCYeSbuYBSp94Go$b11493dc854d029a074e02a4c03eb4daa0452d77e70f33fff4cd8a9e6361e003</td>
        <td>Patsy Hauck</td>
        <td>1985-11-19</td>
    </tr>
    <tr>
        <td>6</td>
        <td>CaryRogahn@gmail.com</td>
        <td>(914) 513-1752</td>
        <td>949 Courtney Rest, Herbertport, NV 89459</td>
        <td>caryrogahn</td>
        <td>pbkdf2:sha256:260000$TCGuQXJUvfFHNOqB$4bed9dca3cca19960e5e17587cdcbce168b281bb789fc23841a4a718f1022bee</td>
        <td>Cary Rogahn</td>
        <td>1977-11-07</td>
    </tr>
    <tr>
        <td>7</td>
        <td>MargaritoCarter@gmail.com</td>
        <td>(651) 219-1947</td>
        <td>370 Cole Wall, New Karrie, MD 64577</td>
        <td>margaritocarter</td>
        <td>pbkdf2:sha256:260000$IJdCq1OzFbl5gRTu$44df121195da286b49c7b86a9e3e75663bcf5bfdcff5f9d29d0a028a1278920b</td>
        <td>Margarito Carter</td>
        <td>1981-09-14</td>
    </tr>
    <tr>
        <td>8</td>
        <td>JewellHowell@gmail.com</td>
        <td>(972) 212-9178</td>
        <td>Apt. 161 329 Lowe Ridges, North Ward, RI 52815</td>
        <td>jewellhowell</td>
        <td>pbkdf2:sha256:260000$Ihq7jyXgpm2Wi0Y7$98591629b3c9f5d539ddb39751b43f285b274a21121bbcf2a59383bc2296e90f</td>
        <td>Jewell Howell</td>
        <td>1986-09-25</td>
    </tr>
    <tr>
        <td>9</td>
        <td>TraciHessel@gmail.com</td>
        <td>(860) 469-0000</td>
        <td>768 Kendall Plain, Trevaport, PA 63853</td>
        <td>tracihessel</td>
        <td>pbkdf2:sha256:260000$0KZgBMAH7SahCkyT$4e4e48775b6a2ea4c0e71d3c7a0723d7b2c1f9bb69e5081a4da8f435ad1d4abd</td>
        <td>Traci Hessel</td>
        <td>1981-01-19</td>
    </tr>
    <tr>
        <td>10</td>
        <td>JcO&#x27;Connell@gmail.com</td>
        <td>(313) 203-3152 x1920</td>
        <td>Suite 931 29113 Greenfelder Village, West Jennifer, MA 59678</td>
        <td>jcoconnell</td>
        <td>pbkdf2:sha256:260000$XXurdpVeKtk500lm$12a9aca0c459cc5381a327afea5eccfb146c22a0d439eb3dc7b9babda6517f72</td>
        <td>Jc O&#x27;Connell</td>
        <td>2004-09-30</td>
    </tr>
    <tr>
        <td>11</td>
        <td>jordansmith@gmail.com</td>
        <td>+1-159-948-2854</td>
        <td>4224 Julie Parkway Apt. 566East Kyle, NC 39027</td>
        <td>jordansmith</td>
        <td>pbkdf2:sha256:260000$MlTzOquqhnyZpZWs$92467ba1a9c1fb8a99317d1835d5bc5bb5849699359eea4d484dd5e29ca42837</td>
        <td>Jordan Smith</td>
        <td>1971-11-14</td>
    </tr>
    <tr>
        <td>12</td>
        <td>philipparsons@gmail.com</td>
        <td>+1-157-882-1598x01997</td>
        <td>06873 Jeffrey CornersJeffreymouth, MT 43173</td>
        <td>philipparsons</td>
        <td>pbkdf2:sha256:260000$qxyUWA1si4Qx41Ej$aa5d458220d0fb1e54afc1d70c8b6c2f6cb726bd074d45a634f8f0b14a84d9de</td>
        <td>Philip Parsons</td>
        <td>1998-02-15</td>
    </tr>
    <tr>
        <td>13</td>
        <td>dannyharper@gmail.com</td>
        <td>8250637858</td>
        <td>759 Walsh Points Suite 080Phillipsfort, AK 90255</td>
        <td>dannyharper</td>
        <td>pbkdf2:sha256:260000$J8GSCB7qLwsbxDQt$1da76007e1b03b875b236cbbee717c6d076fc81c2ed93beb70ba00d3dc646fcf</td>
        <td>Danny Harper</td>
        <td>1997-08-18</td>
    </tr>
    <tr>
        <td>14</td>
        <td>kimberlytate@gmail.com</td>
        <td>001-478-741-7148x82365</td>
        <td>981 Jimenez Mountains Suite 216East Tanyastad, VA 82883</td>
        <td>kimberlytate</td>
        <td>pbkdf2:sha256:260000$1EXYCRe1Uh05vVaN$59ca1653a8895970b670cba7389f12342236b96239090549cae9bcbfd4a9df6b</td>
        <td>Kimberly Tate</td>
        <td>2004-06-05</td>
    </tr>
    <tr>
        <td>15</td>
        <td>robertbarnes@gmail.com</td>
        <td>(903)153-9594x571</td>
        <td>79035 Love Underpass Apt. 229West Jorge, KY 37117</td>
        <td>robertbarnes</td>
        <td>pbkdf2:sha256:260000$8nACDusY1TdqokqP$7daf116a6c6d4fe0ab04851fad955f3888c983fe060da605a692855a9c35cb01</td>
        <td>Robert Barnes</td>
        <td>1969-01-20</td>
    </tr>
    <tr>
        <td>16</td>
        <td>stephaniesmith@gmail.com</td>
        <td>6391915108</td>
        <td>011 Dawn Fords Suite 474Jennifermouth, RI 69604</td>
        <td>stephaniesmith</td>
        <td>pbkdf2:sha256:260000$GYTD0WVcoNMw223Z$7e83e3afd38b63fd864eb49cea65ded74e143f46fde2e9c749c8d4a4c52de38d</td>
        <td>Stephanie Smith</td>
        <td>1965-08-18</td>
    </tr>
    <tr>
        <td>17</td>
        <td>ashleylandry@gmail.com</td>
        <td>314.177.6592</td>
        <td>2663 Davis Locks Apt. 904Mezamouth, ID 61831</td>
        <td>ashleylandry</td>
        <td>pbkdf2:sha256:260000$SjtZCoD4vthe0js1$dd123aab8839b1e2ccbdf0ce72d4c32b79ba6fa7d039f5213f0fc9c09d4281b6</td>
        <td>Ashley Landry</td>
        <td>1994-08-22</td>
    </tr>
    <tr>
        <td>18</td>
        <td>stacyhansen@gmail.com</td>
        <td>+1-005-096-0540x878</td>
        <td>PSC 1116, Box 4648APO AE 80534</td>
        <td>stacyhansen</td>
        <td>pbkdf2:sha256:260000$oipwOCpjMtF3Dhye$9c51d8180081dc7c6920026bc2883a0c1d2b7c77838a81317d55f438043819f8</td>
        <td>Stacy Hansen</td>
        <td>2010-07-15</td>
    </tr>
    <tr>
        <td>19</td>
        <td>michealcline@gmail.com</td>
        <td>609.031.0243x5434</td>
        <td>3129 Roberts Haven Apt. 909Lake Bridgetland, AZ 68618</td>
        <td>michealcline</td>
        <td>pbkdf2:sha256:260000$7gmhwhIdMk47fP8y$a0e0a1926879eb13fde3c75da6e00c7698309bf23e925c0b75663398e9ebe83d</td>
        <td>Micheal Cline</td>
        <td>2002-09-25</td>
    </tr>
    <tr>
        <td>20</td>
        <td>jessicaday@gmail.com</td>
        <td>(491)636-7375</td>
        <td>59263 Alison RapidKimberlyside, WV 40987</td>
        <td>jessicaday</td>
        <td>pbkdf2:sha256:260000$cGfh0jBhVhpL8ltW$f177d96f67f6f6caabcd1851bec965557fb30ffd4dfed559c9238b86d9fea5b1</td>
        <td>Jessica Day</td>
        <td>1960-04-27</td>
    </tr>
    <tr>
        <td>21</td>
        <td>normanrogers@gmail.com</td>
        <td>851-959-4246</td>
        <td>166 Helen Throughway Suite 485West Robertshire, CA 93797</td>
        <td>normanrogers</td>
        <td>pbkdf2:sha256:260000$5OIbhjndYB3YJMSH$d4b1437361e5f4adbec958e8bcdf1afaf29b2a91be73fc32f7ef19defbf90c7f</td>
        <td>Norman Rogers</td>
        <td>1988-10-25</td>
    </tr>
    <tr>
        <td>22</td>
        <td>taylorstout@gmail.com</td>
        <td>(159)459-7175</td>
        <td>USCGC GreenFPO AE 27251</td>
        <td>taylorstout</td>
        <td>pbkdf2:sha256:260000$TAtfK26NaereQR9O$9f9fdaeea77edf41941f5577ccecb0fe7d0d5e84ea79431edda0d785083c3f89</td>
        <td>Taylor Stout</td>
        <td>1999-06-07</td>
    </tr>
    <tr>
        <td>23</td>
        <td>kathybarrera@gmail.com</td>
        <td>9594004325</td>
        <td>7774 Stephen WayWest Brianview, IL 88866</td>
        <td>kathybarrera</td>
        <td>pbkdf2:sha256:260000$iHbE5nGAzl6odNPe$e2a5d32098f3c01a3c152ddfb5afb3c690c2a942a191bdcbe017f1ab4af60f98</td>
        <td>Kathy Barrera</td>
        <td>2001-06-25</td>
    </tr>
    <tr>
        <td>24</td>
        <td>mrs.shannonho@gmail.com</td>
        <td>001-329-404-0086x945</td>
        <td>562 Reid Squares Apt. 874West Brandiburgh, IN 86667</td>
        <td>mrs.shannonho</td>
        <td>pbkdf2:sha256:260000$bVYnjqUMapS78C7F$cdde9083c41f22493c2be324d21dec9430b2c543dd2e86157ca23d7b6193965a</td>
        <td>Mrs. Shannon Ho</td>
        <td>1996-05-24</td>
    </tr>
    <tr>
        <td>25</td>
        <td>angelafritz@gmail.com</td>
        <td>051-084-5564</td>
        <td>90766 Dorsey Walks Suite 930Reginaldchester, ND 05298</td>
        <td>angelafritz</td>
        <td>pbkdf2:sha256:260000$A2Db1hgb9QMwBrBs$04ba0a7b9234e1ec594f6a3486e17efddb7996c09aa0c0feea1b141c3acbf366</td>
        <td>Angela Fritz</td>
        <td>1978-07-20</td>
    </tr>
    <tr>
        <td>26</td>
        <td>kennethlee@gmail.com</td>
        <td>835.029.8906</td>
        <td>PSC 6913, Box 1515APO AE 20751</td>
        <td>kennethlee</td>
        <td>pbkdf2:sha256:260000$zVW0RK4C1eWaAjs9$f0db0bea10c60a754bb4ed72f29dc03d2b4b17e5553c79ac05f13534a253050b</td>
        <td>Kenneth Lee</td>
        <td>1974-12-14</td>
    </tr>
    <tr>
        <td>27</td>
        <td>jimmyzavala@gmail.com</td>
        <td>950.277.2792x6858</td>
        <td>USNS RandolphFPO AA 86503</td>
        <td>jimmyzavala</td>
        <td>pbkdf2:sha256:260000$emXQ5tWyMpcSVSu2$ccdf01d8fed1981d69ccda163ad995fddba466c3e0b1c1750f78fa158a24165e</td>
        <td>Jimmy Zavala</td>
        <td>1985-07-26</td>
    </tr>
    <tr>
        <td>28</td>
        <td>dr.kimalvaradodvm@gmail.com</td>
        <td>101.693.8875x87531</td>
        <td>28466 Elizabeth Spring Suite 794New Michael, NE 04112</td>
        <td>dr.kimalvaradodvm</td>
        <td>pbkdf2:sha256:260000$e9dTzqISMYT9TMSQ$1a34c72295e1390ea494694232c4016267d4717c2be7f531198d1667f812d607</td>
        <td>Dr. Kim Alvarado DVM</td>
        <td>1994-07-26</td>
    </tr>
    <tr>
        <td>29</td>
        <td>melissaingram@gmail.com</td>
        <td>767-278-9759x57519</td>
        <td>27835 Pamela PortsSouth Michael, NM 08348</td>
        <td>melissaingram</td>
        <td>pbkdf2:sha256:260000$aqkePF7LB207VyXp$f17390d84998efeb7389057d8bc13db747e24736e5177d2173d49422b8876400</td>
        <td>Melissa Ingram</td>
        <td>1978-01-07</td>
    </tr>
    <tr>
        <td>30</td>
        <td>chrisrodriguez@gmail.com</td>
        <td>616-562-0549</td>
        <td>743 Anthony StravenueNorth Patricia, WI 45670</td>
        <td>chrisrodriguez</td>
        <td>pbkdf2:sha256:260000$7EIZ7VOITuWiDMD4$98166301eca97745278b502db13db561bcc41349316c14612130db37da5fb2d8</td>
        <td>Chris Rodriguez</td>
        <td>1984-07-14</td>
    </tr>
</table>
```
:::
:::

::: {.cell .code execution_count="121"}
``` python
%%sql
select * from discount
```

::: {.output .stream .stdout}
     * mysql+pymysql://root:***@localhost/
    20 rows affected.
:::

::: {.output .execute_result execution_count="121"}
```{=html}
<table>
    <tr>
        <th>code</th>
        <th>cid</th>
        <th>amount</th>
        <th>startDate</th>
        <th>endDate</th>
    </tr>
    <tr>
        <td>code1</td>
        <td>6</td>
        <td>30</td>
        <td>2023-03-03</td>
        <td>2023-11-22</td>
    </tr>
    <tr>
        <td>code1</td>
        <td>13</td>
        <td>40</td>
        <td>2023-01-11</td>
        <td>2023-09-19</td>
    </tr>
    <tr>
        <td>code10</td>
        <td>18</td>
        <td>40</td>
        <td>2023-01-22</td>
        <td>2023-10-09</td>
    </tr>
    <tr>
        <td>code2</td>
        <td>4</td>
        <td>40</td>
        <td>2023-01-26</td>
        <td>2023-09-19</td>
    </tr>
    <tr>
        <td>code2</td>
        <td>6</td>
        <td>20</td>
        <td>2023-04-19</td>
        <td>2023-09-26</td>
    </tr>
    <tr>
        <td>code2</td>
        <td>12</td>
        <td>30</td>
        <td>2023-04-12</td>
        <td>2023-12-06</td>
    </tr>
    <tr>
        <td>code2</td>
        <td>16</td>
        <td>10</td>
        <td>2023-02-21</td>
        <td>2023-08-06</td>
    </tr>
    <tr>
        <td>code3</td>
        <td>4</td>
        <td>40</td>
        <td>2023-03-10</td>
        <td>2023-09-24</td>
    </tr>
    <tr>
        <td>code4</td>
        <td>30</td>
        <td>50</td>
        <td>2023-02-13</td>
        <td>2023-07-14</td>
    </tr>
    <tr>
        <td>code5</td>
        <td>9</td>
        <td>50</td>
        <td>2023-01-23</td>
        <td>2023-09-01</td>
    </tr>
    <tr>
        <td>code5</td>
        <td>15</td>
        <td>50</td>
        <td>2023-01-01</td>
        <td>2023-10-28</td>
    </tr>
    <tr>
        <td>code6</td>
        <td>20</td>
        <td>50</td>
        <td>2023-01-09</td>
        <td>2023-06-07</td>
    </tr>
    <tr>
        <td>code6</td>
        <td>22</td>
        <td>30</td>
        <td>2023-02-11</td>
        <td>2023-11-27</td>
    </tr>
    <tr>
        <td>code7</td>
        <td>22</td>
        <td>20</td>
        <td>2023-02-07</td>
        <td>2023-11-08</td>
    </tr>
    <tr>
        <td>code7</td>
        <td>24</td>
        <td>40</td>
        <td>2023-02-23</td>
        <td>2023-05-18</td>
    </tr>
    <tr>
        <td>code7</td>
        <td>30</td>
        <td>50</td>
        <td>2023-04-26</td>
        <td>2023-08-10</td>
    </tr>
    <tr>
        <td>code8</td>
        <td>19</td>
        <td>10</td>
        <td>2023-02-08</td>
        <td>2023-12-09</td>
    </tr>
    <tr>
        <td>code8</td>
        <td>22</td>
        <td>40</td>
        <td>2023-04-17</td>
        <td>2023-07-19</td>
    </tr>
    <tr>
        <td>code9</td>
        <td>2</td>
        <td>50</td>
        <td>2023-01-08</td>
        <td>2023-06-10</td>
    </tr>
    <tr>
        <td>code9</td>
        <td>25</td>
        <td>50</td>
        <td>2023-02-08</td>
        <td>2023-12-09</td>
    </tr>
</table>
```
:::
:::

::: {.cell .code execution_count="122"}
``` python
%%sql
select * from feedback
```

::: {.output .stream .stdout}
     * mysql+pymysql://root:***@localhost/
    20 rows affected.
:::

::: {.output .execute_result execution_count="122"}
```{=html}
<table>
    <tr>
        <th>feedbackid</th>
        <th>cid</th>
        <th>category</th>
        <th>content</th>
    </tr>
    <tr>
        <td>1</td>
        <td>5</td>
        <td>Request order cancellation</td>
        <td>Pls cancel order</td>
    </tr>
    <tr>
        <td>2</td>
        <td>6</td>
        <td>Missing items</td>
        <td>Where are my pants?</td>
    </tr>
    <tr>
        <td>3</td>
        <td>9</td>
        <td>Request refund</td>
        <td>I want a refund</td>
    </tr>
    <tr>
        <td>4</td>
        <td>10</td>
        <td>Other</td>
        <td>What is this?</td>
    </tr>
    <tr>
        <td>5</td>
        <td>3</td>
        <td>Other</td>
        <td>Ugly website, bad database</td>
    </tr>
    <tr>
        <td>6</td>
        <td>6</td>
        <td>Request order cancellation</td>
        <td>Pls cancel order</td>
    </tr>
    <tr>
        <td>7</td>
        <td>15</td>
        <td>Missing items</td>
        <td>Where are my shoes?</td>
    </tr>
    <tr>
        <td>8</td>
        <td>30</td>
        <td>Other</td>
        <td>Boo</td>
    </tr>
    <tr>
        <td>9</td>
        <td>27</td>
        <td>Request order cancellation</td>
        <td>Pls cancel order</td>
    </tr>
    <tr>
        <td>10</td>
        <td>7</td>
        <td>Missing items</td>
        <td>Hat missing</td>
    </tr>
    <tr>
        <td>11</td>
        <td>10</td>
        <td>Missing items</td>
        <td>Dog missing</td>
    </tr>
    <tr>
        <td>12</td>
        <td>22</td>
        <td>Missing items</td>
        <td>Where are my clothes?</td>
    </tr>
    <tr>
        <td>13</td>
        <td>30</td>
        <td>Other</td>
        <td>Yeah</td>
    </tr>
    <tr>
        <td>14</td>
        <td>11</td>
        <td>Request refund</td>
        <td>money pls</td>
    </tr>
    <tr>
        <td>15</td>
        <td>29</td>
        <td>Other</td>
        <td>i like</td>
    </tr>
    <tr>
        <td>16</td>
        <td>12</td>
        <td>Request order cancellation</td>
        <td>Pls cancel order</td>
    </tr>
    <tr>
        <td>17</td>
        <td>17</td>
        <td>Request order cancellation</td>
        <td>Pls cancel order</td>
    </tr>
    <tr>
        <td>18</td>
        <td>29</td>
        <td>Request order cancellation</td>
        <td>Pls cancel order</td>
    </tr>
    <tr>
        <td>19</td>
        <td>17</td>
        <td>Other</td>
        <td>Hello :))</td>
    </tr>
    <tr>
        <td>20</td>
        <td>1</td>
        <td>Missing items</td>
        <td>Where are my shirts?</td>
    </tr>
</table>
```
:::
:::

::: {.cell .code execution_count="123"}
``` python
%%sql
select * from sale
```

::: {.output .stream .stdout}
     * mysql+pymysql://root:***@localhost/
    20 rows affected.
:::

::: {.output .execute_result execution_count="123"}
```{=html}
<table>
    <tr>
        <th>saleid</th>
        <th>amount</th>
        <th>startDate</th>
        <th>endDate</th>
        <th>description</th>
    </tr>
    <tr>
        <td>1</td>
        <td>40</td>
        <td>2022-03-18</td>
        <td>2022-07-17</td>
        <td>The first sale</td>
    </tr>
    <tr>
        <td>2</td>
        <td>10</td>
        <td>2022-04-27</td>
        <td>2022-11-08</td>
        <td>The second sale</td>
    </tr>
    <tr>
        <td>3</td>
        <td>50</td>
        <td>2022-01-25</td>
        <td>2022-09-11</td>
        <td>The third sale</td>
    </tr>
    <tr>
        <td>4</td>
        <td>10</td>
        <td>2022-02-27</td>
        <td>2022-11-02</td>
        <td>The fourth sale</td>
    </tr>
    <tr>
        <td>5</td>
        <td>30</td>
        <td>2022-01-25</td>
        <td>2022-10-15</td>
        <td>The fifth sale</td>
    </tr>
    <tr>
        <td>6</td>
        <td>20</td>
        <td>2022-02-05</td>
        <td>2022-06-05</td>
        <td>The sizth sale</td>
    </tr>
    <tr>
        <td>7</td>
        <td>40</td>
        <td>2022-04-18</td>
        <td>2022-10-06</td>
        <td>The seventh sale</td>
    </tr>
    <tr>
        <td>8</td>
        <td>50</td>
        <td>2022-03-25</td>
        <td>2022-12-02</td>
        <td>The eighth sale</td>
    </tr>
    <tr>
        <td>9</td>
        <td>40</td>
        <td>2022-04-09</td>
        <td>2022-11-04</td>
        <td>The ninth sale</td>
    </tr>
    <tr>
        <td>10</td>
        <td>10</td>
        <td>2022-04-17</td>
        <td>2022-05-10</td>
        <td>The tenth sale</td>
    </tr>
    <tr>
        <td>11</td>
        <td>10</td>
        <td>2022-04-02</td>
        <td>2022-10-28</td>
        <td>The eleventh sale</td>
    </tr>
    <tr>
        <td>12</td>
        <td>50</td>
        <td>2022-03-08</td>
        <td>2022-05-22</td>
        <td>The twefth sale</td>
    </tr>
    <tr>
        <td>13</td>
        <td>30</td>
        <td>2022-03-08</td>
        <td>2022-06-28</td>
        <td>The thirteenth sale</td>
    </tr>
    <tr>
        <td>14</td>
        <td>20</td>
        <td>2022-03-10</td>
        <td>2022-06-07</td>
        <td>The fourteenth sale</td>
    </tr>
    <tr>
        <td>15</td>
        <td>40</td>
        <td>2022-01-27</td>
        <td>2022-05-19</td>
        <td>The fifteenth sale</td>
    </tr>
    <tr>
        <td>16</td>
        <td>10</td>
        <td>2022-02-07</td>
        <td>2022-10-04</td>
        <td>The sixteenth sale</td>
    </tr>
    <tr>
        <td>17</td>
        <td>30</td>
        <td>2022-03-02</td>
        <td>2022-09-27</td>
        <td>The seventeenth sale</td>
    </tr>
    <tr>
        <td>18</td>
        <td>40</td>
        <td>2022-01-04</td>
        <td>2022-10-07</td>
        <td>The eighteenth sale</td>
    </tr>
    <tr>
        <td>19</td>
        <td>40</td>
        <td>2022-04-26</td>
        <td>2022-06-22</td>
        <td>The nineteenth sale</td>
    </tr>
    <tr>
        <td>20</td>
        <td>20</td>
        <td>2022-02-05</td>
        <td>2022-12-23</td>
        <td>The twentieth sale</td>
    </tr>
</table>
```
:::
:::

::: {.cell .code execution_count="124"}
``` python
%%sql
select * from designer
```

::: {.output .stream .stdout}
     * mysql+pymysql://root:***@localhost/
    20 rows affected.
:::

::: {.output .execute_result execution_count="124"}
```{=html}
<table>
    <tr>
        <th>designerid</th>
        <th>name</th>
        <th>bio</th>
        <th>website</th>
    </tr>
    <tr>
        <td>1</td>
        <td>ADbros</td>
        <td>Official UGC creator and developer!</td>
        <td>https://www.roblox.com/users/23988269/profile</td>
    </tr>
    <tr>
        <td>2</td>
        <td>cyutsee</td>
        <td>certified idiot</td>
        <td>https://www.roblox.com/users/36897775/profile</td>
    </tr>
    <tr>
        <td>3</td>
        <td>FrancklinDay</td>
        <td>UGC Creator/ 3d artist</td>
        <td>https://www.roblox.com/users/155179916/profile</td>
    </tr>
    <tr>
        <td>4</td>
        <td>AshCraft</td>
        <td>hi im a 3D artist and a UGC creator</td>
        <td>https://www.roblox.com/users/13461533/profile</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Racoamigos</td>
        <td>Bienvenidos Racoamigos! Este es un canal de Fans y amigos de mi canal de youtube: Raconidas.</td>
        <td>https://www.roblox.com/groups/4559112/Racoamigos#!/about</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Barack Obama</td>
        <td>Dad, husband, President, citizen.</td>
        <td>https://twitter.com/BarackObama</td>
    </tr>
    <tr>
        <td>7</td>
        <td>Elon Musk</td>
        <td>Joined June 2009</td>
        <td>https://twitter.com/elonmusk</td>
    </tr>
    <tr>
        <td>8</td>
        <td>Justin Bieber</td>
        <td>JUSTICE the album out now</td>
        <td>https://twitter.com/justinbieber</td>
    </tr>
    <tr>
        <td>9</td>
        <td>Katy Perry</td>
        <td>LOVE is the key that unlocks every door</td>
        <td>https://twitter.com/katyperry</td>
    </tr>
    <tr>
        <td>10</td>
        <td>Rihanna</td>
        <td>Not followed by anyone youâ€™re following</td>
        <td>https://twitter.com/rihanna</td>
    </tr>
    <tr>
        <td>11</td>
        <td>Christiano Ronaldo</td>
        <td>This Privacy Policy addresses the collection and use of personal information - </td>
        <td>https://twitter.com/Cristiano</td>
    </tr>
    <tr>
        <td>12</td>
        <td>Taylor Swift</td>
        <td>I&#x27;m the problem, it&#x27;s me</td>
        <td>https://twitter.com/taylorswift13</td>
    </tr>
    <tr>
        <td>13</td>
        <td>Lady Gaga</td>
        <td>THE CHROMATICA BALL </td>
        <td>https://twitter.com/ladygaga</td>
    </tr>
    <tr>
        <td>14</td>
        <td>Ellen DeGeneres</td>
        <td>This account doesnâ€™t exist</td>
        <td>https://twitter.com/TheEllenShow</td>
    </tr>
    <tr>
        <td>15</td>
        <td>Kim Kardashian</td>
        <td>@SKIMS@SKKN@SKKYPartners</td>
        <td>https://twitter.com/KimKardashian</td>
    </tr>
    <tr>
        <td>16</td>
        <td>Selena Gomez</td>
        <td>My Mind &amp; Me is out now.</td>
        <td>https://twitter.com/selenagomez</td>
    </tr>
    <tr>
        <td>17</td>
        <td>Justin Timberlake</td>
        <td>I write hooks but Iâ€™m really just here for the bridge.</td>
        <td>https://twitter.com/jtimberlake</td>
    </tr>
    <tr>
        <td>18</td>
        <td>Bill Gates</td>
        <td>Sharing things I&#x27;m learning through my foundation work and other interests.</td>
        <td>https://twitter.com/BillGates</td>
    </tr>
    <tr>
        <td>19</td>
        <td>Neymar Jr.</td>
        <td>Filho de Deus, Pai, Feliz e Ousado !</td>
        <td>https://twitter.com/neymarjr</td>
    </tr>
    <tr>
        <td>20</td>
        <td>Tim Henson</td>
        <td>@Polyphia</td>
        <td>https://twitter.com/thew6rst</td>
    </tr>
</table>
```
:::
:::

::: {.cell .code execution_count="125"}
``` python
%%sql
select * from product
```

::: {.output .stream .stdout}
     * mysql+pymysql://root:***@localhost/
    56 rows affected.
:::

::: {.output .execute_result execution_count="125"}
```{=html}
<table>
    <tr>
        <th>pid</th>
        <th>name</th>
        <th>stock</th>
        <th>type</th>
        <th>size</th>
        <th>price</th>
        <th>designerid</th>
        <th>addDate</th>
        <th>image</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Huge T-shirt</td>
        <td>89</td>
        <td>T-Shirt</td>
        <td>S</td>
        <td>49.9</td>
        <td>1</td>
        <td>2023-03-14</td>
        <td>clothes/dec324bf-c2ff-4c7b-8d5a-96f17be58eb8.jpg</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Huge T-shirt</td>
        <td>50</td>
        <td>T-Shirt</td>
        <td>L</td>
        <td>51.9</td>
        <td>1</td>
        <td>2023-03-14</td>
        <td>clothes/dec324bf-c2ff-4c7b-8d5a-96f17be58eb8.jpg</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Ossified Longsleeve</td>
        <td>96</td>
        <td>Longsleeve</td>
        <td>S</td>
        <td>38.9</td>
        <td>2</td>
        <td>2023-03-18</td>
        <td>clothes/36b4e957-021d-4a48-aaea-25dff54e162c.jpg</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Ossified Longsleeve</td>
        <td>35</td>
        <td>Longsleeve</td>
        <td>M</td>
        <td>40.9</td>
        <td>2</td>
        <td>2023-03-18</td>
        <td>clothes/36b4e957-021d-4a48-aaea-25dff54e162c.jpg</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Breezy Longsleeve</td>
        <td>75</td>
        <td>Longsleeve</td>
        <td>M</td>
        <td>52.9</td>
        <td>2</td>
        <td>2023-01-13</td>
        <td>clothes/38bf9790-f653-453b-96b4-72a298413eb7.jpg</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Breezy Longsleeve</td>
        <td>30</td>
        <td>Longsleeve</td>
        <td>L</td>
        <td>54.9</td>
        <td>2</td>
        <td>2023-01-13</td>
        <td>clothes/38bf9790-f653-453b-96b4-72a298413eb7.jpg</td>
    </tr>
    <tr>
        <td>7</td>
        <td>Imaginary Shirt</td>
        <td>60</td>
        <td>Shirt</td>
        <td>L</td>
        <td>48.9</td>
        <td>3</td>
        <td>2023-01-23</td>
        <td>clothes/6050dd9d-c65c-4c57-9b07-00328b8aace3.jpg</td>
    </tr>
    <tr>
        <td>8</td>
        <td>Imaginary Shirt</td>
        <td>20</td>
        <td>Shirt</td>
        <td>XXL</td>
        <td>50.9</td>
        <td>3</td>
        <td>2023-01-23</td>
        <td>clothes/6050dd9d-c65c-4c57-9b07-00328b8aace3.jpg</td>
    </tr>
    <tr>
        <td>9</td>
        <td>General Shoes</td>
        <td>56</td>
        <td>Shoes</td>
        <td>S</td>
        <td>22.9</td>
        <td>4</td>
        <td>2023-02-27</td>
        <td>clothes/b3586849-9c97-4f0b-81cf-80664fe91e08.jpg</td>
    </tr>
    <tr>
        <td>10</td>
        <td>General Shoes</td>
        <td>20</td>
        <td>Shoes</td>
        <td>M</td>
        <td>24.9</td>
        <td>4</td>
        <td>2023-02-27</td>
        <td>clothes/b3586849-9c97-4f0b-81cf-80664fe91e08.jpg</td>
    </tr>
    <tr>
        <td>11</td>
        <td>Ill Pants</td>
        <td>78</td>
        <td>Pants</td>
        <td>XS</td>
        <td>30.9</td>
        <td>5</td>
        <td>2023-01-05</td>
        <td>clothes/824224ea-df38-446b-a01e-ca078906bb93.jpg</td>
    </tr>
    <tr>
        <td>12</td>
        <td>Ill Pants</td>
        <td>33</td>
        <td>Pants</td>
        <td>XL</td>
        <td>32.9</td>
        <td>5</td>
        <td>2023-01-05</td>
        <td>clothes/824224ea-df38-446b-a01e-ca078906bb93.jpg</td>
    </tr>
    <tr>
        <td>13</td>
        <td>Concerned Outwear</td>
        <td>82</td>
        <td>Outwear</td>
        <td>S</td>
        <td>99.9</td>
        <td>6</td>
        <td>2023-01-17</td>
        <td>clothes/81c52306-df14-4e69-af05-775fce77e7e4.jpg</td>
    </tr>
    <tr>
        <td>14</td>
        <td>Concerned Outwear</td>
        <td>92</td>
        <td>Outwear</td>
        <td>M</td>
        <td>101.9</td>
        <td>6</td>
        <td>2023-01-17</td>
        <td>clothes/81c52306-df14-4e69-af05-775fce77e7e4.jpg</td>
    </tr>
    <tr>
        <td>15</td>
        <td>Voracious Dress</td>
        <td>79</td>
        <td>Dress</td>
        <td>S</td>
        <td>59.9</td>
        <td>7</td>
        <td>2023-03-12</td>
        <td>clothes/95dd0618-9a05-4abe-853c-fa6c3fa9bcce.jpg</td>
    </tr>
    <tr>
        <td>16</td>
        <td>Voracious Dress</td>
        <td>37</td>
        <td>Dress</td>
        <td>M</td>
        <td>61.9</td>
        <td>7</td>
        <td>2023-03-12</td>
        <td>clothes/95dd0618-9a05-4abe-853c-fa6c3fa9bcce.jpg</td>
    </tr>
    <tr>
        <td>17</td>
        <td>Teeny Longsleeve</td>
        <td>36</td>
        <td>Longsleeve</td>
        <td>S</td>
        <td>24.9</td>
        <td>8</td>
        <td>2023-01-08</td>
        <td>clothes/3982179b-1523-4cea-868d-4dd3e71779b0.jpg</td>
    </tr>
    <tr>
        <td>18</td>
        <td>Teeny Longsleeve</td>
        <td>85</td>
        <td>Longsleeve</td>
        <td>M</td>
        <td>26.9</td>
        <td>8</td>
        <td>2023-01-08</td>
        <td>clothes/3982179b-1523-4cea-868d-4dd3e71779b0.jpg</td>
    </tr>
    <tr>
        <td>19</td>
        <td>Selective Hat</td>
        <td>87</td>
        <td>Hat</td>
        <td>S</td>
        <td>99.9</td>
        <td>9</td>
        <td>2023-01-20</td>
        <td>clothes/c09d1e27-97cf-4d81-b156-ab5226966875.jpg</td>
    </tr>
    <tr>
        <td>20</td>
        <td>Selective Hat</td>
        <td>79</td>
        <td>Hat</td>
        <td>M</td>
        <td>101.9</td>
        <td>9</td>
        <td>2023-01-20</td>
        <td>clothes/c09d1e27-97cf-4d81-b156-ab5226966875.jpg</td>
    </tr>
    <tr>
        <td>21</td>
        <td>Jagged Blouse</td>
        <td>41</td>
        <td>Blouse</td>
        <td>M</td>
        <td>65.9</td>
        <td>10</td>
        <td>2023-01-24</td>
        <td>clothes/4ef0dece-adfc-4036-ad34-922d607d4bd5.jpg</td>
    </tr>
    <tr>
        <td>22</td>
        <td>Jagged Blouse</td>
        <td>71</td>
        <td>Blouse</td>
        <td>XL</td>
        <td>67.9</td>
        <td>10</td>
        <td>2023-01-24</td>
        <td>clothes/4ef0dece-adfc-4036-ad34-922d607d4bd5.jpg</td>
    </tr>
    <tr>
        <td>23</td>
        <td>Elated Dress</td>
        <td>52</td>
        <td>Dress</td>
        <td>S</td>
        <td>52.9</td>
        <td>11</td>
        <td>2023-01-03</td>
        <td>clothes/6b779a54-4cdc-4205-ba1f-9597c779a683.jpg</td>
    </tr>
    <tr>
        <td>24</td>
        <td>Elated Dress</td>
        <td>23</td>
        <td>Dress</td>
        <td>M</td>
        <td>54.9</td>
        <td>11</td>
        <td>2023-01-03</td>
        <td>clothes/6b779a54-4cdc-4205-ba1f-9597c779a683.jpg</td>
    </tr>
    <tr>
        <td>25</td>
        <td>Telling Longsleeve</td>
        <td>80</td>
        <td>Longsleeve</td>
        <td>S</td>
        <td>98.9</td>
        <td>12</td>
        <td>2023-01-07</td>
        <td>clothes/21d5734b-6bb8-4fe2-92fb-187bf8eed730.jpg</td>
    </tr>
    <tr>
        <td>26</td>
        <td>Telling Longsleeve</td>
        <td>44</td>
        <td>Longsleeve</td>
        <td>M</td>
        <td>100.9</td>
        <td>12</td>
        <td>2023-01-07</td>
        <td>clothes/21d5734b-6bb8-4fe2-92fb-187bf8eed730.jpg</td>
    </tr>
    <tr>
        <td>27</td>
        <td>Succinct T-shirt</td>
        <td>64</td>
        <td>T-Shirt</td>
        <td>S</td>
        <td>44.9</td>
        <td>13</td>
        <td>2023-01-04</td>
        <td>clothes/a8fbce59-ff02-4109-b9d3-51bbc87399ec.jpg</td>
    </tr>
    <tr>
        <td>28</td>
        <td>Succinct T-shirt</td>
        <td>35</td>
        <td>T-Shirt</td>
        <td>M</td>
        <td>46.9</td>
        <td>13</td>
        <td>2023-01-04</td>
        <td>clothes/a8fbce59-ff02-4109-b9d3-51bbc87399ec.jpg</td>
    </tr>
    <tr>
        <td>29</td>
        <td>Resonant Skirt</td>
        <td>28</td>
        <td>Skirt</td>
        <td>S</td>
        <td>81.9</td>
        <td>14</td>
        <td>2023-02-07</td>
        <td>clothes/667a7349-f0a7-43bc-bb70-246b61e6354b.jpg</td>
    </tr>
    <tr>
        <td>30</td>
        <td>Resonant Skirt</td>
        <td>58</td>
        <td>Skirt</td>
        <td>M</td>
        <td>83.9</td>
        <td>14</td>
        <td>2023-02-07</td>
        <td>clothes/667a7349-f0a7-43bc-bb70-246b61e6354b.jpg</td>
    </tr>
    <tr>
        <td>31</td>
        <td>Milky T-shirt</td>
        <td>88</td>
        <td>T-Shirt</td>
        <td>L</td>
        <td>76.9</td>
        <td>15</td>
        <td>2023-01-22</td>
        <td>clothes/844083b8-2610-413c-9c41-2bd1440b797e.jpg</td>
    </tr>
    <tr>
        <td>32</td>
        <td>Milky T-shirt</td>
        <td>84</td>
        <td>T-Shirt</td>
        <td>XL</td>
        <td>78.9</td>
        <td>15</td>
        <td>2023-01-22</td>
        <td>clothes/844083b8-2610-413c-9c41-2bd1440b797e.jpg</td>
    </tr>
    <tr>
        <td>33</td>
        <td>Curious Longsleeve</td>
        <td>60</td>
        <td>Longsleeve</td>
        <td>S</td>
        <td>26.9</td>
        <td>16</td>
        <td>2023-03-27</td>
        <td>clothes/80c77dd2-8dfb-4674-9c83-aa36f86c6794.jpg</td>
    </tr>
    <tr>
        <td>34</td>
        <td>Curious Longsleeve</td>
        <td>74</td>
        <td>Longsleeve</td>
        <td>M</td>
        <td>28.9</td>
        <td>16</td>
        <td>2023-03-27</td>
        <td>clothes/80c77dd2-8dfb-4674-9c83-aa36f86c6794.jpg</td>
    </tr>
    <tr>
        <td>35</td>
        <td>Wild T-shirt</td>
        <td>54</td>
        <td>T-Shirt</td>
        <td>S</td>
        <td>68.9</td>
        <td>17</td>
        <td>2023-02-10</td>
        <td>clothes/b88b9d84-7e62-4ffa-be92-854dc1804349.jpg</td>
    </tr>
    <tr>
        <td>36</td>
        <td>Wild T-shirt</td>
        <td>94</td>
        <td>T-Shirt</td>
        <td>M</td>
        <td>70.9</td>
        <td>17</td>
        <td>2023-02-10</td>
        <td>clothes/b88b9d84-7e62-4ffa-be92-854dc1804349.jpg</td>
    </tr>
    <tr>
        <td>37</td>
        <td>Heavy Shoes</td>
        <td>89</td>
        <td>Shoes</td>
        <td>XL</td>
        <td>24.9</td>
        <td>18</td>
        <td>2023-01-24</td>
        <td>clothes/38bec7b5-9585-4cee-acb9-dcbb09d0b118.jpg</td>
    </tr>
    <tr>
        <td>38</td>
        <td>Heavy Shoes</td>
        <td>75</td>
        <td>Shoes</td>
        <td>XXL</td>
        <td>26.9</td>
        <td>18</td>
        <td>2023-01-24</td>
        <td>clothes/38bec7b5-9585-4cee-acb9-dcbb09d0b118.jpg</td>
    </tr>
    <tr>
        <td>39</td>
        <td>Seemly Polo</td>
        <td>25</td>
        <td>Polo</td>
        <td>S</td>
        <td>37.9</td>
        <td>19</td>
        <td>2023-02-03</td>
        <td>clothes/0925fb2c-d509-4791-9770-48b398c68511.jpg</td>
    </tr>
    <tr>
        <td>40</td>
        <td>Seemly Polo</td>
        <td>46</td>
        <td>Polo</td>
        <td>M</td>
        <td>39.9</td>
        <td>19</td>
        <td>2023-02-03</td>
        <td>clothes/0925fb2c-d509-4791-9770-48b398c68511.jpg</td>
    </tr>
    <tr>
        <td>41</td>
        <td>Spurious Pants</td>
        <td>95</td>
        <td>Pants</td>
        <td>S</td>
        <td>45.9</td>
        <td>20</td>
        <td>2023-03-23</td>
        <td>clothes/1a08f33a-2ff4-4fb8-920b-8ff514bcdda8.jpg</td>
    </tr>
    <tr>
        <td>42</td>
        <td>Spurious Pants</td>
        <td>38</td>
        <td>Pants</td>
        <td>M</td>
        <td>47.9</td>
        <td>20</td>
        <td>2023-03-23</td>
        <td>clothes/1a08f33a-2ff4-4fb8-920b-8ff514bcdda8.jpg</td>
    </tr>
    <tr>
        <td>43</td>
        <td>Gleaming Pants</td>
        <td>82</td>
        <td>Pants</td>
        <td>S</td>
        <td>82.9</td>
        <td>20</td>
        <td>2023-01-08</td>
        <td>clothes/ed0bd341-69e8-4a25-a5e7-11d0976543ca.jpg</td>
    </tr>
    <tr>
        <td>44</td>
        <td>Gleaming Pants</td>
        <td>53</td>
        <td>Pants</td>
        <td>M</td>
        <td>84.9</td>
        <td>20</td>
        <td>2023-01-08</td>
        <td>clothes/ed0bd341-69e8-4a25-a5e7-11d0976543ca.jpg</td>
    </tr>
    <tr>
        <td>45</td>
        <td>Reflective Hoodie</td>
        <td>95</td>
        <td>Hoodie</td>
        <td>S</td>
        <td>36.9</td>
        <td>2</td>
        <td>2023-03-04</td>
        <td>clothes/f9870e0c-7906-4c63-87fe-fc12b8cd8d38.jpg</td>
    </tr>
    <tr>
        <td>46</td>
        <td>Reflective Hoodie</td>
        <td>36</td>
        <td>Hoodie</td>
        <td>M</td>
        <td>38.9</td>
        <td>2</td>
        <td>2023-03-04</td>
        <td>clothes/f9870e0c-7906-4c63-87fe-fc12b8cd8d38.jpg</td>
    </tr>
    <tr>
        <td>47</td>
        <td>Nimble Hat</td>
        <td>26</td>
        <td>Hat</td>
        <td>XS</td>
        <td>47.9</td>
        <td>12</td>
        <td>2023-03-05</td>
        <td>clothes/eb5b5b2d-1db8-4a2a-9ab7-53067df7558b.jpg</td>
    </tr>
    <tr>
        <td>48</td>
        <td>Nimble Hat</td>
        <td>32</td>
        <td>Hat</td>
        <td>M</td>
        <td>49.9</td>
        <td>12</td>
        <td>2023-03-05</td>
        <td>clothes/eb5b5b2d-1db8-4a2a-9ab7-53067df7558b.jpg</td>
    </tr>
    <tr>
        <td>49</td>
        <td>Guiltless T-shirt</td>
        <td>80</td>
        <td>T-Shirt</td>
        <td>S</td>
        <td>35.9</td>
        <td>20</td>
        <td>2023-03-25</td>
        <td>clothes/6567c49d-5cd4-44b2-9824-5c8f4caed18f.jpg</td>
    </tr>
    <tr>
        <td>50</td>
        <td>Guiltless T-shirt</td>
        <td>41</td>
        <td>T-Shirt</td>
        <td>L</td>
        <td>37.9</td>
        <td>20</td>
        <td>2023-03-25</td>
        <td>clothes/6567c49d-5cd4-44b2-9824-5c8f4caed18f.jpg</td>
    </tr>
    <tr>
        <td>51</td>
        <td>Frail Hat</td>
        <td>91</td>
        <td>Hat</td>
        <td>S</td>
        <td>44.9</td>
        <td>17</td>
        <td>2023-03-02</td>
        <td>clothes/14d9f39c-48f5-4da6-bea4-b9f8b94633ed.jpg</td>
    </tr>
    <tr>
        <td>52</td>
        <td>Frail Hat</td>
        <td>77</td>
        <td>Hat</td>
        <td>M</td>
        <td>46.9</td>
        <td>17</td>
        <td>2023-03-02</td>
        <td>clothes/14d9f39c-48f5-4da6-bea4-b9f8b94633ed.jpg</td>
    </tr>
    <tr>
        <td>53</td>
        <td>Valuable Shirt</td>
        <td>31</td>
        <td>Shirt</td>
        <td>M</td>
        <td>96.9</td>
        <td>2</td>
        <td>2023-02-06</td>
        <td>kids_clothes/0cd501af-4cce-460d-9431-637bf0d95499.jpg</td>
    </tr>
    <tr>
        <td>54</td>
        <td>Dangerous Pants</td>
        <td>38</td>
        <td>Pants</td>
        <td>M</td>
        <td>9.9</td>
        <td>14</td>
        <td>2023-03-26</td>
        <td>kids_clothes/bbbff34f-4830-4dc0-819a-45ef69a70e76.jpg</td>
    </tr>
    <tr>
        <td>55</td>
        <td>Childlike Dress</td>
        <td>87</td>
        <td>Dress</td>
        <td>M</td>
        <td>37.9</td>
        <td>15</td>
        <td>2023-01-23</td>
        <td>kids_clothes/41b5fb92-5be4-4000-952c-5d074fd4be6a.jpg</td>
    </tr>
    <tr>
        <td>56</td>
        <td>Alike Outwear</td>
        <td>69</td>
        <td>Outwear</td>
        <td>M</td>
        <td>48.9</td>
        <td>13</td>
        <td>2023-02-27</td>
        <td>kids_clothes/d1e39cbf-1bf5-4dbe-8b57-a0697eafa4fe.jpg</td>
    </tr>
</table>
```
:::
:::

::: {.cell .code execution_count="126"}
``` python
%%sql
select * from onsale
```

::: {.output .stream .stdout}
     * mysql+pymysql://root:***@localhost/
    20 rows affected.
:::

::: {.output .execute_result execution_count="126"}
```{=html}
<table>
    <tr>
        <th>saleid</th>
        <th>pid</th>
    </tr>
    <tr>
        <td>1</td>
        <td>46</td>
    </tr>
    <tr>
        <td>2</td>
        <td>13</td>
    </tr>
    <tr>
        <td>2</td>
        <td>16</td>
    </tr>
    <tr>
        <td>2</td>
        <td>29</td>
    </tr>
    <tr>
        <td>2</td>
        <td>38</td>
    </tr>
    <tr>
        <td>2</td>
        <td>55</td>
    </tr>
    <tr>
        <td>3</td>
        <td>1</td>
    </tr>
    <tr>
        <td>3</td>
        <td>35</td>
    </tr>
    <tr>
        <td>4</td>
        <td>30</td>
    </tr>
    <tr>
        <td>4</td>
        <td>52</td>
    </tr>
    <tr>
        <td>4</td>
        <td>53</td>
    </tr>
    <tr>
        <td>5</td>
        <td>35</td>
    </tr>
    <tr>
        <td>6</td>
        <td>6</td>
    </tr>
    <tr>
        <td>6</td>
        <td>46</td>
    </tr>
    <tr>
        <td>7</td>
        <td>3</td>
    </tr>
    <tr>
        <td>8</td>
        <td>22</td>
    </tr>
    <tr>
        <td>8</td>
        <td>42</td>
    </tr>
    <tr>
        <td>9</td>
        <td>52</td>
    </tr>
    <tr>
        <td>16</td>
        <td>53</td>
    </tr>
    <tr>
        <td>20</td>
        <td>43</td>
    </tr>
</table>
```
:::
:::

::: {.cell .code execution_count="127"}
``` python
%%sql
select * from review
```

::: {.output .stream .stdout}
     * mysql+pymysql://root:***@localhost/
    20 rows affected.
:::

::: {.output .execute_result execution_count="127"}
```{=html}
<table>
    <tr>
        <th>pid</th>
        <th>cid</th>
        <th>rating</th>
        <th>comment</th>
        <th>date</th>
    </tr>
    <tr>
        <td>1</td>
        <td>13</td>
        <td>4</td>
        <td>Good</td>
        <td>2022-03-05</td>
    </tr>
    <tr>
        <td>3</td>
        <td>14</td>
        <td>3</td>
        <td>Okay</td>
        <td>2022-02-27</td>
    </tr>
    <tr>
        <td>4</td>
        <td>5</td>
        <td>2</td>
        <td>Bad</td>
        <td>2022-03-10</td>
    </tr>
    <tr>
        <td>4</td>
        <td>21</td>
        <td>5</td>
        <td>Excellent</td>
        <td>2022-02-16</td>
    </tr>
    <tr>
        <td>5</td>
        <td>8</td>
        <td>4</td>
        <td>Good</td>
        <td>2022-03-25</td>
    </tr>
    <tr>
        <td>11</td>
        <td>20</td>
        <td>4</td>
        <td>Good</td>
        <td>2022-04-09</td>
    </tr>
    <tr>
        <td>11</td>
        <td>29</td>
        <td>4</td>
        <td>Good</td>
        <td>2022-01-08</td>
    </tr>
    <tr>
        <td>12</td>
        <td>19</td>
        <td>2</td>
        <td>Bad</td>
        <td>2022-01-10</td>
    </tr>
    <tr>
        <td>14</td>
        <td>23</td>
        <td>3</td>
        <td>Okay</td>
        <td>2022-02-10</td>
    </tr>
    <tr>
        <td>26</td>
        <td>22</td>
        <td>4</td>
        <td>Good</td>
        <td>2022-02-09</td>
    </tr>
    <tr>
        <td>34</td>
        <td>23</td>
        <td>4</td>
        <td>Good</td>
        <td>2022-04-04</td>
    </tr>
    <tr>
        <td>40</td>
        <td>3</td>
        <td>1</td>
        <td>Terrible</td>
        <td>2022-03-07</td>
    </tr>
    <tr>
        <td>42</td>
        <td>28</td>
        <td>3</td>
        <td>Okay</td>
        <td>2022-03-16</td>
    </tr>
    <tr>
        <td>43</td>
        <td>28</td>
        <td>2</td>
        <td>Bad</td>
        <td>2022-04-16</td>
    </tr>
    <tr>
        <td>45</td>
        <td>18</td>
        <td>4</td>
        <td>Good</td>
        <td>2022-02-05</td>
    </tr>
    <tr>
        <td>45</td>
        <td>20</td>
        <td>4</td>
        <td>Good</td>
        <td>2022-02-20</td>
    </tr>
    <tr>
        <td>47</td>
        <td>2</td>
        <td>4</td>
        <td>Good</td>
        <td>2022-02-03</td>
    </tr>
    <tr>
        <td>52</td>
        <td>3</td>
        <td>5</td>
        <td>Excellent</td>
        <td>2022-01-21</td>
    </tr>
    <tr>
        <td>55</td>
        <td>22</td>
        <td>5</td>
        <td>Excellent</td>
        <td>2022-03-11</td>
    </tr>
    <tr>
        <td>56</td>
        <td>29</td>
        <td>3</td>
        <td>Okay</td>
        <td>2022-03-15</td>
    </tr>
</table>
```
:::
:::

::: {.cell .code execution_count="128"}
``` python
%%sql
select * from color
```

::: {.output .stream .stdout}
     * mysql+pymysql://root:***@localhost/
    69 rows affected.
:::

::: {.output .execute_result execution_count="128"}
```{=html}
<table>
    <tr>
        <th>pid</th>
        <th>color</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Blue</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Blue</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Black</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Pink</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Black</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Pink</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Brown</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Brown</td>
    </tr>
    <tr>
        <td>7</td>
        <td>White</td>
    </tr>
    <tr>
        <td>8</td>
        <td>White</td>
    </tr>
    <tr>
        <td>9</td>
        <td>Pink</td>
    </tr>
    <tr>
        <td>10</td>
        <td>Pink</td>
    </tr>
    <tr>
        <td>11</td>
        <td>Gray</td>
    </tr>
    <tr>
        <td>12</td>
        <td>Gray</td>
    </tr>
    <tr>
        <td>13</td>
        <td>Brown</td>
    </tr>
    <tr>
        <td>14</td>
        <td>Brown</td>
    </tr>
    <tr>
        <td>15</td>
        <td>Red</td>
    </tr>
    <tr>
        <td>15</td>
        <td>White</td>
    </tr>
    <tr>
        <td>16</td>
        <td>Red</td>
    </tr>
    <tr>
        <td>16</td>
        <td>White</td>
    </tr>
    <tr>
        <td>17</td>
        <td>Black</td>
    </tr>
    <tr>
        <td>18</td>
        <td>Black</td>
    </tr>
    <tr>
        <td>19</td>
        <td>Gray</td>
    </tr>
    <tr>
        <td>20</td>
        <td>Gray</td>
    </tr>
    <tr>
        <td>21</td>
        <td>White</td>
    </tr>
    <tr>
        <td>22</td>
        <td>White</td>
    </tr>
    <tr>
        <td>23</td>
        <td>Blue</td>
    </tr>
    <tr>
        <td>24</td>
        <td>Blue</td>
    </tr>
    <tr>
        <td>25</td>
        <td>Blue</td>
    </tr>
    <tr>
        <td>25</td>
        <td>White</td>
    </tr>
    <tr>
        <td>26</td>
        <td>Blue</td>
    </tr>
    <tr>
        <td>26</td>
        <td>White</td>
    </tr>
    <tr>
        <td>27</td>
        <td>Blue</td>
    </tr>
    <tr>
        <td>28</td>
        <td>Blue</td>
    </tr>
    <tr>
        <td>29</td>
        <td>Blue</td>
    </tr>
    <tr>
        <td>30</td>
        <td>Blue</td>
    </tr>
    <tr>
        <td>31</td>
        <td>Red</td>
    </tr>
    <tr>
        <td>32</td>
        <td>Red</td>
    </tr>
    <tr>
        <td>33</td>
        <td>White</td>
    </tr>
    <tr>
        <td>34</td>
        <td>White</td>
    </tr>
    <tr>
        <td>35</td>
        <td>Blue</td>
    </tr>
    <tr>
        <td>35</td>
        <td>White</td>
    </tr>
    <tr>
        <td>36</td>
        <td>Blue</td>
    </tr>
    <tr>
        <td>36</td>
        <td>White</td>
    </tr>
    <tr>
        <td>37</td>
        <td>Black</td>
    </tr>
    <tr>
        <td>37</td>
        <td>White</td>
    </tr>
    <tr>
        <td>38</td>
        <td>Black</td>
    </tr>
    <tr>
        <td>38</td>
        <td>White</td>
    </tr>
    <tr>
        <td>39</td>
        <td>Red</td>
    </tr>
    <tr>
        <td>40</td>
        <td>Red</td>
    </tr>
    <tr>
        <td>41</td>
        <td>Black</td>
    </tr>
    <tr>
        <td>42</td>
        <td>Black</td>
    </tr>
    <tr>
        <td>43</td>
        <td>Blue</td>
    </tr>
    <tr>
        <td>44</td>
        <td>Blue</td>
    </tr>
    <tr>
        <td>45</td>
        <td>Green</td>
    </tr>
    <tr>
        <td>46</td>
        <td>Green</td>
    </tr>
    <tr>
        <td>47</td>
        <td>Black</td>
    </tr>
    <tr>
        <td>47</td>
        <td>White</td>
    </tr>
    <tr>
        <td>48</td>
        <td>Black</td>
    </tr>
    <tr>
        <td>48</td>
        <td>White</td>
    </tr>
    <tr>
        <td>49</td>
        <td>Yellow</td>
    </tr>
    <tr>
        <td>50</td>
        <td>Yellow</td>
    </tr>
    <tr>
        <td>51</td>
        <td>Brown</td>
    </tr>
    <tr>
        <td>52</td>
        <td>Brown</td>
    </tr>
    <tr>
        <td>53</td>
        <td>White</td>
    </tr>
    <tr>
        <td>54</td>
        <td>Blue</td>
    </tr>
    <tr>
        <td>55</td>
        <td>Blue</td>
    </tr>
    <tr>
        <td>55</td>
        <td>White</td>
    </tr>
    <tr>
        <td>56</td>
        <td>Purple</td>
    </tr>
</table>
```
:::
:::

::: {.cell .code execution_count="129"}
``` python
%%sql
select * from category
```

::: {.output .stream .stdout}
     * mysql+pymysql://root:***@localhost/
    102 rows affected.
:::

::: {.output .execute_result execution_count="129"}
```{=html}
<table>
    <tr>
        <th>pid</th>
        <th>category</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>1</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Men</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Men</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>7</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>7</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>8</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>8</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>9</td>
        <td>Men</td>
    </tr>
    <tr>
        <td>9</td>
        <td>Shoes</td>
    </tr>
    <tr>
        <td>10</td>
        <td>Men</td>
    </tr>
    <tr>
        <td>10</td>
        <td>Shoes</td>
    </tr>
    <tr>
        <td>11</td>
        <td>Bottom</td>
    </tr>
    <tr>
        <td>11</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>12</td>
        <td>Bottom</td>
    </tr>
    <tr>
        <td>12</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>13</td>
        <td>Men</td>
    </tr>
    <tr>
        <td>13</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>14</td>
        <td>Men</td>
    </tr>
    <tr>
        <td>14</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>15</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>16</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>17</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>17</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>18</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>18</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>19</td>
        <td>Hat</td>
    </tr>
    <tr>
        <td>19</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>20</td>
        <td>Hat</td>
    </tr>
    <tr>
        <td>20</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>21</td>
        <td>Men</td>
    </tr>
    <tr>
        <td>22</td>
        <td>Men</td>
    </tr>
    <tr>
        <td>23</td>
        <td>Men</td>
    </tr>
    <tr>
        <td>24</td>
        <td>Men</td>
    </tr>
    <tr>
        <td>25</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>25</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>26</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>26</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>27</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>27</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>28</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>28</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>29</td>
        <td>Bottom</td>
    </tr>
    <tr>
        <td>29</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>30</td>
        <td>Bottom</td>
    </tr>
    <tr>
        <td>30</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>31</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>31</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>32</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>32</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>33</td>
        <td>Men</td>
    </tr>
    <tr>
        <td>33</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>34</td>
        <td>Men</td>
    </tr>
    <tr>
        <td>34</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>35</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>35</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>36</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>36</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>37</td>
        <td>Men</td>
    </tr>
    <tr>
        <td>37</td>
        <td>Shoes</td>
    </tr>
    <tr>
        <td>38</td>
        <td>Men</td>
    </tr>
    <tr>
        <td>38</td>
        <td>Shoes</td>
    </tr>
    <tr>
        <td>39</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>39</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>40</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>40</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>41</td>
        <td>Bottom</td>
    </tr>
    <tr>
        <td>41</td>
        <td>Men</td>
    </tr>
    <tr>
        <td>42</td>
        <td>Bottom</td>
    </tr>
    <tr>
        <td>42</td>
        <td>Men</td>
    </tr>
    <tr>
        <td>43</td>
        <td>Bottom</td>
    </tr>
    <tr>
        <td>43</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>44</td>
        <td>Bottom</td>
    </tr>
    <tr>
        <td>44</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>45</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>45</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>46</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>46</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>47</td>
        <td>Hat</td>
    </tr>
    <tr>
        <td>47</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>48</td>
        <td>Hat</td>
    </tr>
    <tr>
        <td>48</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>49</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>49</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>50</td>
        <td>Top</td>
    </tr>
    <tr>
        <td>50</td>
        <td>Women</td>
    </tr>
    <tr>
        <td>51</td>
        <td>Hat</td>
    </tr>
    <tr>
        <td>51</td>
        <td>Men</td>
    </tr>
    <tr>
        <td>52</td>
        <td>Hat</td>
    </tr>
    <tr>
        <td>52</td>
        <td>Men</td>
    </tr>
    <tr>
        <td>53</td>
        <td>Kids</td>
    </tr>
    <tr>
        <td>54</td>
        <td>Kids</td>
    </tr>
    <tr>
        <td>55</td>
        <td>Kids</td>
    </tr>
    <tr>
        <td>56</td>
        <td>Kids</td>
    </tr>
</table>
```
:::
:::

::: {.cell .code execution_count="130"}
``` python
%%sql
select * from cart
```

::: {.output .stream .stdout}
     * mysql+pymysql://root:***@localhost/
    20 rows affected.
:::

::: {.output .execute_result execution_count="130"}
```{=html}
<table>
    <tr>
        <th>cartid</th>
        <th>totalPrice</th>
        <th>cid</th>
        <th>date</th>
        <th>shipCost</th>
        <th>status</th>
    </tr>
    <tr>
        <td>1</td>
        <td>331.3</td>
        <td>28</td>
        <td>2023-02-07</td>
        <td>8.0</td>
        <td>Delivered</td>
    </tr>
    <tr>
        <td>2</td>
        <td>393.2</td>
        <td>30</td>
        <td>2023-02-02</td>
        <td>1.0</td>
        <td>Delivered</td>
    </tr>
    <tr>
        <td>3</td>
        <td>1130.4</td>
        <td>2</td>
        <td>2023-03-28</td>
        <td>2.0</td>
        <td>Canceled</td>
    </tr>
    <tr>
        <td>4</td>
        <td>438.0</td>
        <td>24</td>
        <td>2023-01-04</td>
        <td>10.0</td>
        <td>Delivered</td>
    </tr>
    <tr>
        <td>5</td>
        <td>203.8</td>
        <td>14</td>
        <td>2023-01-21</td>
        <td>4.0</td>
        <td>Out for delivery</td>
    </tr>
    <tr>
        <td>6</td>
        <td>761.1</td>
        <td>12</td>
        <td>2023-03-02</td>
        <td>3.0</td>
        <td>Canceled</td>
    </tr>
    <tr>
        <td>7</td>
        <td>289.2</td>
        <td>10</td>
        <td>2023-02-19</td>
        <td>1.0</td>
        <td>Out for delivery</td>
    </tr>
    <tr>
        <td>8</td>
        <td>207.5</td>
        <td>28</td>
        <td>2023-03-28</td>
        <td>7.0</td>
        <td>Out for delivery</td>
    </tr>
    <tr>
        <td>9</td>
        <td>1182.2</td>
        <td>30</td>
        <td>2023-01-08</td>
        <td>1.0</td>
        <td>Out for delivery</td>
    </tr>
    <tr>
        <td>10</td>
        <td>74.7</td>
        <td>11</td>
        <td>2023-03-17</td>
        <td>1.0</td>
        <td>Out for delivery</td>
    </tr>
    <tr>
        <td>11</td>
        <td>191.6</td>
        <td>14</td>
        <td>2023-03-26</td>
        <td>7.0</td>
        <td>Canceled</td>
    </tr>
    <tr>
        <td>12</td>
        <td>569.2</td>
        <td>29</td>
        <td>2023-03-01</td>
        <td>6.0</td>
        <td>Delivered</td>
    </tr>
    <tr>
        <td>13</td>
        <td>644.9</td>
        <td>25</td>
        <td>2023-03-13</td>
        <td>3.0</td>
        <td>Delivered</td>
    </tr>
    <tr>
        <td>14</td>
        <td>605.2</td>
        <td>18</td>
        <td>2023-03-13</td>
        <td>3.0</td>
        <td>Delivered</td>
    </tr>
    <tr>
        <td>15</td>
        <td>259.6</td>
        <td>15</td>
        <td>2023-01-13</td>
        <td>4.0</td>
        <td>Out for delivery</td>
    </tr>
    <tr>
        <td>16</td>
        <td>81.9</td>
        <td>28</td>
        <td>2023-02-18</td>
        <td>8.0</td>
        <td>Canceled</td>
    </tr>
    <tr>
        <td>17</td>
        <td>319.5</td>
        <td>24</td>
        <td>2023-02-07</td>
        <td>6.0</td>
        <td>Delivered</td>
    </tr>
    <tr>
        <td>18</td>
        <td>395.6</td>
        <td>16</td>
        <td>2023-01-17</td>
        <td>2.0</td>
        <td>Out for delivery</td>
    </tr>
    <tr>
        <td>19</td>
        <td>49.8</td>
        <td>26</td>
        <td>2023-03-28</td>
        <td>6.0</td>
        <td>Out for delivery</td>
    </tr>
    <tr>
        <td>20</td>
        <td>848.9</td>
        <td>6</td>
        <td>2023-03-21</td>
        <td>8.0</td>
        <td>Delivered</td>
    </tr>
</table>
```
:::
:::

::: {.cell .code execution_count="131"}
``` python
%%sql
select * from favourite
```

::: {.output .stream .stdout}
     * mysql+pymysql://root:***@localhost/
    30 rows affected.
:::

::: {.output .execute_result execution_count="131"}
```{=html}
<table>
    <tr>
        <th>pid</th>
        <th>cid</th>
    </tr>
    <tr>
        <td>2</td>
        <td>3</td>
    </tr>
    <tr>
        <td>48</td>
        <td>4</td>
    </tr>
    <tr>
        <td>43</td>
        <td>5</td>
    </tr>
    <tr>
        <td>4</td>
        <td>6</td>
    </tr>
    <tr>
        <td>6</td>
        <td>6</td>
    </tr>
    <tr>
        <td>14</td>
        <td>7</td>
    </tr>
    <tr>
        <td>17</td>
        <td>7</td>
    </tr>
    <tr>
        <td>23</td>
        <td>10</td>
    </tr>
    <tr>
        <td>32</td>
        <td>10</td>
    </tr>
    <tr>
        <td>35</td>
        <td>10</td>
    </tr>
    <tr>
        <td>6</td>
        <td>13</td>
    </tr>
    <tr>
        <td>26</td>
        <td>13</td>
    </tr>
    <tr>
        <td>34</td>
        <td>14</td>
    </tr>
    <tr>
        <td>21</td>
        <td>16</td>
    </tr>
    <tr>
        <td>8</td>
        <td>17</td>
    </tr>
    <tr>
        <td>37</td>
        <td>17</td>
    </tr>
    <tr>
        <td>39</td>
        <td>17</td>
    </tr>
    <tr>
        <td>53</td>
        <td>17</td>
    </tr>
    <tr>
        <td>1</td>
        <td>18</td>
    </tr>
    <tr>
        <td>13</td>
        <td>19</td>
    </tr>
    <tr>
        <td>36</td>
        <td>23</td>
    </tr>
    <tr>
        <td>24</td>
        <td>24</td>
    </tr>
    <tr>
        <td>8</td>
        <td>26</td>
    </tr>
    <tr>
        <td>3</td>
        <td>27</td>
    </tr>
    <tr>
        <td>36</td>
        <td>27</td>
    </tr>
    <tr>
        <td>43</td>
        <td>27</td>
    </tr>
    <tr>
        <td>45</td>
        <td>27</td>
    </tr>
    <tr>
        <td>11</td>
        <td>29</td>
    </tr>
    <tr>
        <td>2</td>
        <td>30</td>
    </tr>
    <tr>
        <td>52</td>
        <td>30</td>
    </tr>
</table>
```
:::
:::

::: {.cell .code execution_count="132"}
``` python
%%sql
select * from addedto
```

::: {.output .stream .stdout}
     * mysql+pymysql://root:***@localhost/
    48 rows affected.
:::

::: {.output .execute_result execution_count="132"}
```{=html}
<table>
    <tr>
        <th>pid</th>
        <th>cartid</th>
        <th>quantity</th>
    </tr>
    <tr>
        <td>2</td>
        <td>20</td>
        <td>1</td>
    </tr>
    <tr>
        <td>5</td>
        <td>1</td>
        <td>3</td>
    </tr>
    <tr>
        <td>5</td>
        <td>2</td>
        <td>5</td>
    </tr>
    <tr>
        <td>5</td>
        <td>9</td>
        <td>5</td>
    </tr>
    <tr>
        <td>5</td>
        <td>13</td>
        <td>5</td>
    </tr>
    <tr>
        <td>6</td>
        <td>6</td>
        <td>2</td>
    </tr>
    <tr>
        <td>6</td>
        <td>17</td>
        <td>4</td>
    </tr>
    <tr>
        <td>8</td>
        <td>9</td>
        <td>3</td>
    </tr>
    <tr>
        <td>10</td>
        <td>4</td>
        <td>4</td>
    </tr>
    <tr>
        <td>10</td>
        <td>10</td>
        <td>3</td>
    </tr>
    <tr>
        <td>10</td>
        <td>12</td>
        <td>3</td>
    </tr>
    <tr>
        <td>13</td>
        <td>3</td>
        <td>2</td>
    </tr>
    <tr>
        <td>13</td>
        <td>6</td>
        <td>4</td>
    </tr>
    <tr>
        <td>13</td>
        <td>14</td>
        <td>5</td>
    </tr>
    <tr>
        <td>14</td>
        <td>5</td>
        <td>2</td>
    </tr>
    <tr>
        <td>16</td>
        <td>15</td>
        <td>2</td>
    </tr>
    <tr>
        <td>17</td>
        <td>13</td>
        <td>3</td>
    </tr>
    <tr>
        <td>19</td>
        <td>17</td>
        <td>1</td>
    </tr>
    <tr>
        <td>20</td>
        <td>13</td>
        <td>3</td>
    </tr>
    <tr>
        <td>22</td>
        <td>15</td>
        <td>2</td>
    </tr>
    <tr>
        <td>24</td>
        <td>3</td>
        <td>3</td>
    </tr>
    <tr>
        <td>24</td>
        <td>7</td>
        <td>3</td>
    </tr>
    <tr>
        <td>25</td>
        <td>9</td>
        <td>5</td>
    </tr>
    <tr>
        <td>25</td>
        <td>12</td>
        <td>5</td>
    </tr>
    <tr>
        <td>25</td>
        <td>18</td>
        <td>4</td>
    </tr>
    <tr>
        <td>28</td>
        <td>9</td>
        <td>4</td>
    </tr>
    <tr>
        <td>29</td>
        <td>3</td>
        <td>5</td>
    </tr>
    <tr>
        <td>29</td>
        <td>16</td>
        <td>1</td>
    </tr>
    <tr>
        <td>30</td>
        <td>6</td>
        <td>3</td>
    </tr>
    <tr>
        <td>31</td>
        <td>4</td>
        <td>3</td>
    </tr>
    <tr>
        <td>31</td>
        <td>20</td>
        <td>4</td>
    </tr>
    <tr>
        <td>32</td>
        <td>2</td>
        <td>1</td>
    </tr>
    <tr>
        <td>32</td>
        <td>20</td>
        <td>2</td>
    </tr>
    <tr>
        <td>34</td>
        <td>8</td>
        <td>2</td>
    </tr>
    <tr>
        <td>34</td>
        <td>14</td>
        <td>2</td>
    </tr>
    <tr>
        <td>36</td>
        <td>3</td>
        <td>3</td>
    </tr>
    <tr>
        <td>37</td>
        <td>2</td>
        <td>2</td>
    </tr>
    <tr>
        <td>37</td>
        <td>7</td>
        <td>5</td>
    </tr>
    <tr>
        <td>37</td>
        <td>19</td>
        <td>2</td>
    </tr>
    <tr>
        <td>39</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>42</td>
        <td>3</td>
        <td>3</td>
    </tr>
    <tr>
        <td>42</td>
        <td>14</td>
        <td>1</td>
    </tr>
    <tr>
        <td>43</td>
        <td>9</td>
        <td>1</td>
    </tr>
    <tr>
        <td>43</td>
        <td>20</td>
        <td>4</td>
    </tr>
    <tr>
        <td>47</td>
        <td>11</td>
        <td>4</td>
    </tr>
    <tr>
        <td>48</td>
        <td>8</td>
        <td>3</td>
    </tr>
    <tr>
        <td>49</td>
        <td>4</td>
        <td>3</td>
    </tr>
    <tr>
        <td>51</td>
        <td>1</td>
        <td>3</td>
    </tr>
</table>
```
:::
:::

::: {.cell .markdown}
### Section F: Stored Program & Queries Script {#section-f-stored-program--queries-script}
:::

::: {.cell .markdown}
```{=html}
<div class="alert alert-block alert-warning">
Insert your Section F from phase 2 here. No further changes required / allowed.
</div>
```
:::

::: {.cell .markdown}
#### Query 1
:::

::: {.cell .markdown}
This is the filter for the store\'s search function, allows users to
browse more easily.

-   Check if either name or designer name contains search term
-   Check if product matches requirements on type, size, price, color,
    category
-   Sort the products based on added date / price
-   Returns the id of the product.
:::

::: {.cell .code execution_count="133"}
``` python
%%sql
drop procedure if exists search;

create procedure search(in _search varchar(50), in _type varchar(20), in _size varchar(4), in _price float,
                        in _color varchar(10), in _category varchar(20), in _sortby varchar(10))
begin
    select distinct product.pid, price, addDate
    from product, color, category, designer
    where product.pid = color.pid and product.pid = category.pid and designer.designerid = product.designerid
    and (_search is null or product.name like CONCAT('%', _search , '%') or designer.name like CONCAT('%', _search , '%')) 
    and (_type is null or type = _type)
    and (_size is null or size = _size)
    and (_price is null or price < _price)
    and (_color is null or color = _color)
    and (_category is null or category = _category)
    order by (case _sortby
        when "pricemin" then price
        when "pricemax" then -price
        else -addDate
    end);
end;

call search(null,null,null,50,"Black","Men","pricemin")
```

::: {.output .stream .stdout}
     * mysql+pymysql://root:***@localhost/
    0 rows affected.
    0 rows affected.
    6 rows affected.
:::

::: {.output .execute_result execution_count="133"}
```{=html}
<table>
    <tr>
        <th>pid</th>
        <th>price</th>
        <th>addDate</th>
    </tr>
    <tr>
        <td>37</td>
        <td>24.9</td>
        <td>2023-01-24</td>
    </tr>
    <tr>
        <td>38</td>
        <td>26.9</td>
        <td>2023-01-24</td>
    </tr>
    <tr>
        <td>3</td>
        <td>38.9</td>
        <td>2023-03-18</td>
    </tr>
    <tr>
        <td>4</td>
        <td>40.9</td>
        <td>2023-03-18</td>
    </tr>
    <tr>
        <td>41</td>
        <td>45.9</td>
        <td>2023-03-23</td>
    </tr>
    <tr>
        <td>42</td>
        <td>47.9</td>
        <td>2023-03-23</td>
    </tr>
</table>
```
:::
:::

::: {.cell .markdown}
#### Query 2
:::

::: {.cell .markdown}
What are the products bought most often by each customer? For each
customer who has bought a product, list the customer\'s id and name, the
products\'s id, name and quantity bought by the customer. Arrange the
quantity in descending order.

This could be useful in evaluating what customers are more interested in
and recommending products.
:::

::: {.cell .code execution_count="134"}
``` python
%%sql
select customer.cid, customer.name as cname, product.pid, product.name as pname, sum(quantity)
from customer, cart, (
    select cart.cartid, addedto.pid as pid, sum(quantity) as quantity
    from cart, addedto
    where cart.cartid = addedto.cartid
    group by cart.cartid,addedto.pid
) t, product
where customer.cid = cart.cid and cart.cartid = t.cartid and t.pid = product.pid and date is not null
group by customer.cid, customer.name, pid
order by cid, sum(quantity) desc
```

::: {.output .stream .stdout}
     * mysql+pymysql://root:***@localhost/
    47 rows affected.
:::

::: {.output .execute_result execution_count="134"}
```{=html}
<table>
    <tr>
        <th>cid</th>
        <th>cname</th>
        <th>pid</th>
        <th>pname</th>
        <th>sum(quantity)</th>
    </tr>
    <tr>
        <td>2</td>
        <td>Catherina Moen</td>
        <td>29</td>
        <td>Resonant Skirt</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Catherina Moen</td>
        <td>24</td>
        <td>Elated Dress</td>
        <td>3</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Catherina Moen</td>
        <td>42</td>
        <td>Spurious Pants</td>
        <td>3</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Catherina Moen</td>
        <td>36</td>
        <td>Wild T-shirt</td>
        <td>3</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Catherina Moen</td>
        <td>13</td>
        <td>Concerned Outwear</td>
        <td>2</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Cary Rogahn</td>
        <td>43</td>
        <td>Gleaming Pants</td>
        <td>4</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Cary Rogahn</td>
        <td>31</td>
        <td>Milky T-shirt</td>
        <td>4</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Cary Rogahn</td>
        <td>32</td>
        <td>Milky T-shirt</td>
        <td>2</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Cary Rogahn</td>
        <td>2</td>
        <td>Huge T-shirt</td>
        <td>1</td>
    </tr>
    <tr>
        <td>10</td>
        <td>Jc O&#x27;Connell</td>
        <td>37</td>
        <td>Heavy Shoes</td>
        <td>5</td>
    </tr>
    <tr>
        <td>10</td>
        <td>Jc O&#x27;Connell</td>
        <td>24</td>
        <td>Elated Dress</td>
        <td>3</td>
    </tr>
    <tr>
        <td>11</td>
        <td>Jordan Smith</td>
        <td>10</td>
        <td>General Shoes</td>
        <td>3</td>
    </tr>
    <tr>
        <td>12</td>
        <td>Philip Parsons</td>
        <td>13</td>
        <td>Concerned Outwear</td>
        <td>4</td>
    </tr>
    <tr>
        <td>12</td>
        <td>Philip Parsons</td>
        <td>30</td>
        <td>Resonant Skirt</td>
        <td>3</td>
    </tr>
    <tr>
        <td>12</td>
        <td>Philip Parsons</td>
        <td>6</td>
        <td>Breezy Longsleeve</td>
        <td>2</td>
    </tr>
    <tr>
        <td>14</td>
        <td>Kimberly Tate</td>
        <td>47</td>
        <td>Nimble Hat</td>
        <td>4</td>
    </tr>
    <tr>
        <td>14</td>
        <td>Kimberly Tate</td>
        <td>14</td>
        <td>Concerned Outwear</td>
        <td>2</td>
    </tr>
    <tr>
        <td>15</td>
        <td>Robert Barnes</td>
        <td>16</td>
        <td>Voracious Dress</td>
        <td>2</td>
    </tr>
    <tr>
        <td>15</td>
        <td>Robert Barnes</td>
        <td>22</td>
        <td>Jagged Blouse</td>
        <td>2</td>
    </tr>
    <tr>
        <td>16</td>
        <td>Stephanie Smith</td>
        <td>25</td>
        <td>Telling Longsleeve</td>
        <td>4</td>
    </tr>
    <tr>
        <td>18</td>
        <td>Stacy Hansen</td>
        <td>13</td>
        <td>Concerned Outwear</td>
        <td>5</td>
    </tr>
    <tr>
        <td>18</td>
        <td>Stacy Hansen</td>
        <td>34</td>
        <td>Curious Longsleeve</td>
        <td>2</td>
    </tr>
    <tr>
        <td>18</td>
        <td>Stacy Hansen</td>
        <td>42</td>
        <td>Spurious Pants</td>
        <td>1</td>
    </tr>
    <tr>
        <td>24</td>
        <td>Mrs. Shannon Ho</td>
        <td>6</td>
        <td>Breezy Longsleeve</td>
        <td>4</td>
    </tr>
    <tr>
        <td>24</td>
        <td>Mrs. Shannon Ho</td>
        <td>10</td>
        <td>General Shoes</td>
        <td>4</td>
    </tr>
    <tr>
        <td>24</td>
        <td>Mrs. Shannon Ho</td>
        <td>31</td>
        <td>Milky T-shirt</td>
        <td>3</td>
    </tr>
    <tr>
        <td>24</td>
        <td>Mrs. Shannon Ho</td>
        <td>49</td>
        <td>Guiltless T-shirt</td>
        <td>3</td>
    </tr>
    <tr>
        <td>24</td>
        <td>Mrs. Shannon Ho</td>
        <td>19</td>
        <td>Selective Hat</td>
        <td>1</td>
    </tr>
    <tr>
        <td>25</td>
        <td>Angela Fritz</td>
        <td>5</td>
        <td>Breezy Longsleeve</td>
        <td>5</td>
    </tr>
    <tr>
        <td>25</td>
        <td>Angela Fritz</td>
        <td>20</td>
        <td>Selective Hat</td>
        <td>3</td>
    </tr>
    <tr>
        <td>25</td>
        <td>Angela Fritz</td>
        <td>17</td>
        <td>Teeny Longsleeve</td>
        <td>3</td>
    </tr>
    <tr>
        <td>26</td>
        <td>Kenneth Lee</td>
        <td>37</td>
        <td>Heavy Shoes</td>
        <td>2</td>
    </tr>
    <tr>
        <td>28</td>
        <td>Dr. Kim Alvarado DVM</td>
        <td>5</td>
        <td>Breezy Longsleeve</td>
        <td>3</td>
    </tr>
    <tr>
        <td>28</td>
        <td>Dr. Kim Alvarado DVM</td>
        <td>51</td>
        <td>Frail Hat</td>
        <td>3</td>
    </tr>
    <tr>
        <td>28</td>
        <td>Dr. Kim Alvarado DVM</td>
        <td>48</td>
        <td>Nimble Hat</td>
        <td>3</td>
    </tr>
    <tr>
        <td>28</td>
        <td>Dr. Kim Alvarado DVM</td>
        <td>34</td>
        <td>Curious Longsleeve</td>
        <td>2</td>
    </tr>
    <tr>
        <td>28</td>
        <td>Dr. Kim Alvarado DVM</td>
        <td>29</td>
        <td>Resonant Skirt</td>
        <td>1</td>
    </tr>
    <tr>
        <td>28</td>
        <td>Dr. Kim Alvarado DVM</td>
        <td>39</td>
        <td>Seemly Polo</td>
        <td>1</td>
    </tr>
    <tr>
        <td>29</td>
        <td>Melissa Ingram</td>
        <td>25</td>
        <td>Telling Longsleeve</td>
        <td>5</td>
    </tr>
    <tr>
        <td>29</td>
        <td>Melissa Ingram</td>
        <td>10</td>
        <td>General Shoes</td>
        <td>3</td>
    </tr>
    <tr>
        <td>30</td>
        <td>Chris Rodriguez</td>
        <td>5</td>
        <td>Breezy Longsleeve</td>
        <td>10</td>
    </tr>
    <tr>
        <td>30</td>
        <td>Chris Rodriguez</td>
        <td>25</td>
        <td>Telling Longsleeve</td>
        <td>5</td>
    </tr>
    <tr>
        <td>30</td>
        <td>Chris Rodriguez</td>
        <td>28</td>
        <td>Succinct T-shirt</td>
        <td>4</td>
    </tr>
    <tr>
        <td>30</td>
        <td>Chris Rodriguez</td>
        <td>8</td>
        <td>Imaginary Shirt</td>
        <td>3</td>
    </tr>
    <tr>
        <td>30</td>
        <td>Chris Rodriguez</td>
        <td>37</td>
        <td>Heavy Shoes</td>
        <td>2</td>
    </tr>
    <tr>
        <td>30</td>
        <td>Chris Rodriguez</td>
        <td>32</td>
        <td>Milky T-shirt</td>
        <td>1</td>
    </tr>
    <tr>
        <td>30</td>
        <td>Chris Rodriguez</td>
        <td>43</td>
        <td>Gleaming Pants</td>
        <td>1</td>
    </tr>
</table>
```
:::
:::

::: {.cell .markdown}
#### Query 3
:::

::: {.cell .markdown}
For every pair of products bought in the same order, count the number of
times that they have been bought together. Rank the pairs by this count
in descending order.

This query finds out which two products are most frequently bought
together and can be used for the recommendation system.
:::

::: {.cell .code execution_count="135"}
``` python
%%sql
select p1.name as 'Product 1', p2.name as 'Product 2', count(*)
from addedto a1, addedto a2, product p1, product p2, cart
where a1.cartid = a2.cartid and a1.pid <> a2.pid
and p1.pid = a1.pid and p2.pid = a2.pid
and cart.cartid = a1.cartid and cart.date is not null
and p1.name < p2.name
group by p1.name, p2.name
order by count(*) desc
```

::: {.output .stream .stdout}
     * mysql+pymysql://root:***@localhost/
    43 rows affected.
:::

::: {.output .execute_result execution_count="135"}
```{=html}
<table>
    <tr>
        <th>Product 1</th>
        <th>Product 2</th>
        <th>count(*)</th>
    </tr>
    <tr>
        <td>Gleaming Pants</td>
        <td>Milky T-shirt</td>
        <td>2</td>
    </tr>
    <tr>
        <td>Concerned Outwear</td>
        <td>Resonant Skirt</td>
        <td>2</td>
    </tr>
    <tr>
        <td>Huge T-shirt</td>
        <td>Milky T-shirt</td>
        <td>2</td>
    </tr>
    <tr>
        <td>Breezy Longsleeve</td>
        <td>Selective Hat</td>
        <td>2</td>
    </tr>
    <tr>
        <td>Concerned Outwear</td>
        <td>Spurious Pants</td>
        <td>2</td>
    </tr>
    <tr>
        <td>Gleaming Pants</td>
        <td>Imaginary Shirt</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Breezy Longsleeve</td>
        <td>Imaginary Shirt</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Breezy Longsleeve</td>
        <td>Concerned Outwear</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Jagged Blouse</td>
        <td>Voracious Dress</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Selective Hat</td>
        <td>Teeny Longsleeve</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Breezy Longsleeve</td>
        <td>Teeny Longsleeve</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Concerned Outwear</td>
        <td>Elated Dress</td>
        <td>1</td>
    </tr>
    <tr>
        <td>General Shoes</td>
        <td>Telling Longsleeve</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Gleaming Pants</td>
        <td>Telling Longsleeve</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Succinct T-shirt</td>
        <td>Telling Longsleeve</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Imaginary Shirt</td>
        <td>Telling Longsleeve</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Breezy Longsleeve</td>
        <td>Telling Longsleeve</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Gleaming Pants</td>
        <td>Succinct T-shirt</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Imaginary Shirt</td>
        <td>Succinct T-shirt</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Elated Dress</td>
        <td>Resonant Skirt</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Breezy Longsleeve</td>
        <td>Resonant Skirt</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Breezy Longsleeve</td>
        <td>Succinct T-shirt</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Guiltless T-shirt</td>
        <td>Milky T-shirt</td>
        <td>1</td>
    </tr>
    <tr>
        <td>General Shoes</td>
        <td>Milky T-shirt</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Heavy Shoes</td>
        <td>Milky T-shirt</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Breezy Longsleeve</td>
        <td>Milky T-shirt</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Concerned Outwear</td>
        <td>Curious Longsleeve</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Spurious Pants</td>
        <td>Wild T-shirt</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Resonant Skirt</td>
        <td>Wild T-shirt</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Elated Dress</td>
        <td>Wild T-shirt</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Concerned Outwear</td>
        <td>Wild T-shirt</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Elated Dress</td>
        <td>Heavy Shoes</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Breezy Longsleeve</td>
        <td>Heavy Shoes</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Frail Hat</td>
        <td>Seemly Polo</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Breezy Longsleeve</td>
        <td>Seemly Polo</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Curious Longsleeve</td>
        <td>Spurious Pants</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Gleaming Pants</td>
        <td>Huge T-shirt</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Resonant Skirt</td>
        <td>Spurious Pants</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Elated Dress</td>
        <td>Spurious Pants</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Breezy Longsleeve</td>
        <td>Gleaming Pants</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Curious Longsleeve</td>
        <td>Nimble Hat</td>
        <td>1</td>
    </tr>
    <tr>
        <td>General Shoes</td>
        <td>Guiltless T-shirt</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Breezy Longsleeve</td>
        <td>Frail Hat</td>
        <td>1</td>
    </tr>
</table>
```
:::
:::

::: {.cell .markdown}
```{=html}
<div class="alert alert-block alert-warning">
<b>Triggers and Events:</b> <br>
Shortlist relevant triggers or scheduled events that are useful for your database system. 
Describe what the trigger/event is for and why it is useful for your DB.
</div>
```
:::

::: {.cell .markdown}
#### Trigger/Event
:::

::: {.cell .markdown}
Calculate total price of each order, trigger when the cart content is
changed.
:::

::: {.cell .code execution_count="136"}
``` python
%%sql
CREATE TRIGGER calcTotalPrice1
AFTER INSERT ON addedto
FOR EACH ROW
BEGIN
    UPDATE cart
    SET totalPrice = totalPrice + (
        select price from product
        where product.pid = new.pid
    )*new.quantity where cartid = new.cartid;
END;

CREATE TRIGGER calcTotalPrice2
AFTER UPDATE ON addedto
FOR EACH ROW
BEGIN
    UPDATE cart
    SET totalPrice = totalPrice + (
        select price from product
        where product.pid = new.pid
    )*new.quantity - (
        select price from product
        where product.pid = old.pid
    )*old.quantity
    where cartid = new.cartid;
END;

CREATE TRIGGER calcTotalPrice3
AFTER DELETE ON addedto
FOR EACH ROW
BEGIN
    UPDATE cart
    SET totalPrice = totalPrice - (
        select price from product
        where product.pid = old.pid
    )*old.quantity where cartid = old.cartid;
END;
```

::: {.output .stream .stdout}
     * mysql+pymysql://root:***@localhost/
    0 rows affected.
    0 rows affected.
    0 rows affected.
:::

::: {.output .execute_result execution_count="136"}
    []
:::
:::

::: {.cell .markdown}
Modify product prices on sales to be used for sales
:::

::: {.cell .code execution_count="137"}
``` python
%%sql
CREATE TRIGGER setSale1
AFTER INSERT ON onsale
FOR EACH ROW
BEGIN
    UPDATE product
        SET price = price /100 * (100-(
            select amount from sale
            where sale.saleid = new.saleid
        ));
END;

CREATE TRIGGER setSale2
AFTER DELETE ON onsale
FOR EACH ROW
BEGIN
    UPDATE product
        SET price = price * 100 / (100-(
            select amount from sale
            where sale.saleid = old.saleid
        ));
END;
```

::: {.output .stream .stdout}
     * mysql+pymysql://root:***@localhost/
    0 rows affected.
    0 rows affected.
:::

::: {.output .execute_result execution_count="137"}
    []
:::
:::

::: {.cell .markdown}
Decrease stock when product is added to order.
:::

::: {.cell .code execution_count="138"}
``` python
%%sql
CREATE TRIGGER setStock1
AFTER INSERT ON addedto
FOR EACH ROW
BEGIN
    UPDATE product
    SET stock = stock - new.quantity where product.pid = new.pid;
END;

CREATE TRIGGER setStock12
AFTER UPDATE ON addedto
FOR EACH ROW
BEGIN
    UPDATE product
    SET stock = stock - new.quantity + old.quantity where product.pid = new.pid;
END;

CREATE TRIGGER setStock3
AFTER DELETE ON addedto
FOR EACH ROW
BEGIN
    UPDATE product
    SET stock = stock + old.quantity where product.pid = old.pid;
END;
```

::: {.output .stream .stdout}
     * mysql+pymysql://root:***@localhost/
    0 rows affected.
    0 rows affected.
    0 rows affected.
:::

::: {.output .execute_result execution_count="138"}
    []
:::
:::

::: {.cell .markdown}
### Section G: Web UI
:::

::: {.cell .markdown}
```{=html}
<div class="alert alert-block alert-warning">
<b>Instructions:</b> <br>
    
For this deliverable you will write a web application that interacts with your database to manage your domain. This application must allow the user to extract specific information from the database, through a user-friendly interface. 
 
Additional marks will be given for good webpage design (in terms of navigation, organization and functionality), and aesthetically pleasing webpage.
 
Your web interface should allow you to demonstrate the CRUD operations:<br>
    
* <b> User Info Page:</b> <br>
    - Allow user to register for a new account
    - Allow registered user to login
    - Allow logged in users to view and edit Profile / Account information
    <br>Other notes:
    - Use sessions to ensure only logged in user may access relevant information of to their account. 
    - Relevant data validation should be done.
*  <b> Search & Browse page (i.e. Read function):</b> <br>
    Upon login, users can search and browse the “data”. 
Searching is likely the most typical action for a user. The user should be presented with a form to specify their search criteria, and based on the results of the underlying database query, will be presented either a list of matching records or a single matching record if only one was found.
<br>It is not necessary to allow user to search for all tables (and they shouldn't be allowed to!). Select a few tables where the search & browse function make sense. You are advised to implement the queries shortlisted in Section F where applicable.
 
*  <b>Pages to demo Create, Update & Delete functions: </b>
   <br> Users should be able to insert, edit and delete their entries! Recommended to just focus on 2 each.
    
Note that you will need to upload ALL source code for the Web UI for this section.
    
You do not need to screen capture every page, but it should demonstrate that you have done all CRUD functions. Note that Login, Register and Profile Edit is NOT sufficient to demonstrate CRUD as it has been guided in ISSL. You should demonstrate CRUD on other tables based on shortlisted purpose of your webfrontend.
</div>
```
:::

::: {.cell .markdown}
Attached relevant image of your FINAL web interface below.
:::

::: {.cell .markdown}
-   Read and edit personal details
:::

::: {.cell .markdown}
`<img src="report/6.png">`{=html}
:::

::: {.cell .markdown}
-   Login and register
:::

::: {.cell .markdown}
`<img src="report/7.png">`{=html}
:::

::: {.cell .markdown}
-   Read from product
-   Insert into cart
-   Insert into favourites
-   Update item quantity in cart (if \'Add to cart\' is clicked more
    than once)
:::

::: {.cell .markdown}
`<img src="report/1.png">`{=html}
:::

::: {.cell .markdown}
-   Product recommendation
:::

::: {.cell .markdown}
`<img src="report/5.png">`{=html}
:::

::: {.cell .markdown}
-   Read from favourites
-   Delete from favourites
:::

::: {.cell .markdown}
`<img src="report/2.png">`{=html}
:::

::: {.cell .markdown}
-   Read from cart
-   Update item quantity
-   Delete items from cart
:::

::: {.cell .markdown}
`<img src="report/3.png">`{=html}
:::

::: {.cell .markdown}
-   Update cart status when placing order
:::

::: {.cell .markdown}
`<img src="report/4.png">`{=html}
:::

::: {.cell .markdown}
### Section H: Project Reflection
:::

::: {.cell .markdown}
```{=html}
<div class="alert alert-block alert-warning">
Write a 1 page reflection here. You may reflect on the following points: <br>
    
* What insights have you gained after completing this project? 
* How has completing the project affected your view of database systems?
* How do you think this project experience would be useful to you in future?
* How do you think you have managed your time for this project? Has the help provided in class been sufficient?
</div>
```
:::

::: {.cell .markdown}
Throughout the project, I have gained valuable knowledge in web
development and database management. I learned that database design is a
crucial step in database management, and that proper database design is
necessary for efficient and organized storage of data and for errorless
operations on the database. I learned to develop a responsive website
and integrate a database system with the website using HTMl, CSS,
Bootstrap and Flask, all of which I had no prior experience with. I also
gained insights on SQL injections and how to prevent them.

Completing this project has enabled me to appreciate the role of
database systems in web development and their significance in data
management. As mentioned above, I now understand even further the
importance of good database design for data storage.

The experiences that I gained from this project would allow me to
develop fully functional websites, which can be very useful as websites
are very powerful modes of communication. The knowledge in database
systems may also assist me in various data management projects or
problems.

I have been successful in managing my time for this project, although
most of the progress mainly came from the initial stress of trying to
develop a full database before realizing the scope. Class discussions
have pointed me to carious security issues which I believe I have
managed to fix, and I think this has been sufficient.
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"skip\"}"}
```{=html}
<hr>
```
© NUS High School of Math & Science
:::
