<h1> scrapy_books</h1>
<i>A Basic Spider to deploy in Scrapy Cloud</i>


The following project is a challenge requested by [Zyte](https://www.zyte.com/)

<h2>Installation</h2>

Click on Code and then on Download Zip.</br>
Or create a folder, open git bash and run:
<pre><code> git clone https://github.com/LucasDamianR/scrapy_books.git </code></pre>

In order to work you must install requirements.txt. 

• cd to the directory where requirements.txt is located</br>
• activate your virtualenv (recommended)</br>
run in your shell:
<pre><code>pip install -r requirements.txt</code></pre>
<h3> Mongodb</h3>
• Download <i>MongoCompass</i> from https://www.mongodb.com/try/download/compass/ </br>
• Create folder <code>C:\data\db</code> </br>
• Exec the mongod.exe


<h2>Running the project</h2>

uncomment in <code>settings.py</code> <code>ITEM_PIPELINES</code></br>
<img src='https://i.ibb.co/5GbbFhS/Whats-App-Image-2022-02-21-at-11-24-36-PM.jpg' />

• cd to the directory where project is located</br>
run in your shell with parameter -o (output file: <code>.json</code>, <code>.csv</code>, <code>.xml</code>)
<pre><code>scrapy crawl books -o books.json</code></pre>

In this example the output like</br>
<img src='https://i.ibb.co/YBxV3nG/Whats-App-Image-2022-02-21-at-11-21-58-PM.jpg' />

</br>
<strong>In MongoCompass view:</strong></br>
<img src='https://i.ibb.co/W5vVjFK/Whats-App-Image-2022-02-21-at-11-28-54-PM.jpg' />
