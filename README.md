<h1>PixelScanner</h1>

<p>PixelScanner is a terminal-based port scanner tool built with Python. It scans open ports on a target IP, focusing on remote access services like SSH, FTP, Telnet, and more. It also provides detailed IP information and offers a clean, user-friendly terminal menu.</p>

<hr />

<h2>Features</h2>

<ul>
  <li>Fast scanning of common ports related to remote access services (SSH, FTP, Telnet, etc.)</li>
  <li>Detailed IP information lookup including Geo-location, ISP, and organization</li>
  <li>Interactive and user-friendly terminal menu interface</li>
  <li>Compatible with Termux and Linux environments</li>
  <li>Easy installation using a simple shell installer script</li>
  <li>Shows progress with clear output and results summary</li>
  <li>Supports scanning a range of ports or specific ports lists</li>
</ul>

<hr />

<h2>Installation</h2>

<p>To install PixelScanner, run the following command in your terminal:</p>

<pre><code>bash -c "$(curl -sL https://github.com/amirebog/pixelscanner/raw/main/install.sh)" @ install
</code></pre>

<p>This command downloads and runs the installer script, setting up everything needed.</p>

<hr />

<h2>Usage</h2>

<p>After installation, launch the scanner with:</p>

<pre><code>python3 pixelscanner.py
</code></pre>

<p>Use the interactive menu to:</p>

<ul>
  <li>Enter target IP address</li>
  <li>Choose scanning options (common ports, full range, specific ports)</li>
  <li>View detailed IP information</li>
  <li>Exit the program</li>
</ul>

<hr />

<h2>Requirements</h2>

<ul>
  <li>Python 3.x</li>
  <li>Built-in Python modules (<code>socket</code>, <code>json</code>, <code>urllib</code>)</li>
  <li>Internet connection for IP info lookup</li>
</ul>

<hr />

<h2>Important Notes</h2>

<ul>
  <li>Ensure Python 3 is installed and accessible via <code>python3</code> command.</li>
  <li>Run this tool only on networks and systems you have permission to scan. Unauthorized scanning is illegal and unethical.</li>
  <li>For best results, use a reliable internet connection.</li>
</ul>

<hr />

<h2>License</h2>

<p>This project is licensed under the MIT License.</p>

<hr />

<h2>Contact</h2>

<p>For questions or support, please open an issue on the GitHub repository:<br />
<a href="https://github.com/amirebog/pixelscanner" target="_blank" rel="noopener noreferrer">https://github.com/amirebog/pixelscanner</a></p>

<hr />

<p>Thank you for using PixelScanner!</p>
