# PyResourceMonitor
<!-- README.md -->

<h1 align="center">🧠 Python Process Monitor</h1>
<p align="center">
  <strong>CPU ve RAM kullanımını anlık olarak izleyen basit bir Python uygulaması</strong><br>
  <em>bir Python scriptini takip etmek için idealdir</em>
</p>

<hr>

<h2>📦 Özellikler</h2>

<ul>
  <li>Gerçek zamanlı <strong>RAM</strong> ve <strong>CPU</strong> kullanımı takibi</li>
  <li>İzlenen script süresi boyunca verileri yazdırma</li>
  <li>psutil ve subprocess kullanımıyla basit ve anlaşılır yapı</li>
</ul>

<hr>

<h2>🚀 Kurulum</h2>

<pre>
git clone [https://github.com/kullanici-adin/python-process-monitor.git](https://github.com/omerfaruk-shp/PyResourceMonitor/)
cd PyResourceMonitor
pip install psutil
</pre>

<hr>

<h2>⚙️ Kullanım</h2>

<pre><code>python monitor.py</code></pre>

> `treckir.py` dosyasının içindeki `target_script` değişkenini izlemek istediğiniz Python scripti ile değiştirin:

```python
target_script = "voskdenemeekran.py"  # İzlenecek scriptin adı
