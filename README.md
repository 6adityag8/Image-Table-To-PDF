<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="ImageTableToPDF_0"></a>Image-Table-To-PDF</h1>
<p class="has-line-data" data-line-start="1" data-line-end="2">A platform where users can convert an uploaded image &amp; a dynamically created table into PDF.</p>
<h3 class="code-line" data-line-start=2 data-line-end=3 ><a id="SETUP_Instructions_2"></a>SETUP Instructions:</h3>
<p class="has-line-data" data-line-start="4" data-line-end="7">1.Install <a href="https://www.atlassian.com/git/tutorials/install-git">Git</a><br>
2.Clone the repository using <code>git clone https://github.com/6adityag8/Image-Table-To-PDF.git</code>.<br>
3.Create a .env file with your environment configuration and non-source controlled sensitive information. You can copy the <a href="https://github.com/6adityag8/Image-Table-To-PDF/blob/master/image_table_to_pdf/.env.example">example file</a> and add the relevent configuration data.</p>
<pre><code class="has-line-data" data-line-start="8" data-line-end="12">cd Image-Table-To-PDF/image_table_to_pdf/
cp .env.example .env
vim .env
</code></pre>
<p class="has-line-data" data-line-start="12" data-line-end="14">3.Install <a href="https://docs.docker.com/get-docker/">Docker</a><br>
4.Move to the parent directory and build the <a href="https://github.com/6adityag8/Image-Table-To-PDF/blob/master/Dockerfile">Dockerfile</a>, using a tag name.</p>
<pre><code class="has-line-data" data-line-start="15" data-line-end="18">cd ..
docker build -t image_table_to_pdf -f Dockerfile .
</code></pre>
<p class="has-line-data" data-line-start="18" data-line-end="19">5.Run the created docker image using the same tag name, previously used.</p>
<pre><code class="has-line-data" data-line-start="20" data-line-end="22">docker run -it -p 8888:8888 image_table_to_pdf
</code></pre>
<p class="has-line-data" data-line-start="22" data-line-end="23">6.Visit <code>localhost:8888</code> in a web browser.</p>