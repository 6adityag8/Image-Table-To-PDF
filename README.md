<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="ImageTableToPDF_0"></a>Image-Table-To-PDF</h1>
<h3 class="code-line" data-line-start=1 data-line-end=2 ><a id="SETUP_Instructions_1"></a>SETUP Instructions:</h3>
<p class="has-line-data" data-line-start="3" data-line-end="6">1.Install <a href="https://www.atlassian.com/git/tutorials/install-git">Git</a><br>
2.Clone the repository using <code>git clone https://github.com/6adityag8/Image-Table-To-PDF.git</code>.<br>
3.Create a .env file with your environment configuration and non-source controlled sensitive information. You can copy the <a href="https://github.com/6adityag8/Image-Table-To-PDF/blob/master/image_table_to_pdf/.env.example">example file</a> and add the relevent configuration data.</p>
<pre><code class="has-line-data" data-line-start="7" data-line-end="11">cd Image-Table-To-PDF/image_table_to_pdf/
cp .env.example .env
vim .env
</code></pre>
<p class="has-line-data" data-line-start="11" data-line-end="13">3.Install <a href="https://docs.docker.com/get-docker/">Docker</a><br>
4.Move to the parent directory and build the <a href="https://github.com/6adityag8/Image-Table-To-PDF/blob/master/Dockerfile">Dockerfile</a>, using a tag name.</p>
<pre><code class="has-line-data" data-line-start="14" data-line-end="17">cd ..
docker build -t image_table_to_pdf -f Dockerfile .
</code></pre>
<p class="has-line-data" data-line-start="17" data-line-end="18">5.Run the created docker image using the same tag name, previously used.</p>
<pre><code class="has-line-data" data-line-start="19" data-line-end="21">docker run -it -p 8888:8888 image_table_to_pdf
</code></pre>
<p class="has-line-data" data-line-start="21" data-line-end="22">6.Visit <code>http://0.0.0.0:8888</code> in a web browser.</p>