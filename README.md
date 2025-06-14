<h1 style="color:#4A90E2; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">PixelScanner</h1>

<p style="font-size:1.1rem; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
PixelScanner is a terminal-based port scanner tool built with Python. It scans open ports on a target IP, focusing on remote access services like SSH, FTP, Telnet, and more. It also provides detailed IP information and offers a clean, user-friendly terminal menu.
</p>

<hr style="border:1px solid #eee;" />

<h2 style="color:#2E86C1;">Features</h2>

<ul style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size:1rem; line-height:1.6;">
  <li>Fast scanning of common ports related to remote access services (SSH, FTP, Telnet, etc.)</li>
  <li>Detailed IP information lookup including Geo-location, ISP, and organization</li>
  <li>Interactive and user-friendly terminal menu interface</li>
  <li>Compatible with Termux and Linux environments</li>
  <li>Easy installation using a simple shell installer script</li>
  <li>Shows progress with clear output and results summary</li>
  <li>Supports scanning a range of ports or specific ports lists</li>
</ul>

<hr style="border:1px solid #eee;" />

<h2 style="color:#2E86C1;">Installation</h2>

<p style="font-family: monospace; background:#f4f4f4; padding:10px; border-radius:5px; display:inline-block;">
bash -c "$(curl -sL https://github.com/amirebog/pixelscanner/raw/main/install.sh)" @ install
</p>

<p style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
This command downloads and runs the installer script, setting up everything needed.
</p>

<hr style="border:1px solid #eee;" />

<h2 style="color:#2E86C1;">Usage</h2>

<p style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
After installation, launch the scanner with:
</p>

<p style="font-family: monospace; background:#f4f4f4; padding:10px; border-radius:5px; display:inline-block;">
python3 pixelscanner.py
</p>

<p>Use the interactive menu to:</p>

<ul style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size:1rem; line-height:1.6;">
  <li>Enter target IP address</li>
  <li>Choose scanning options (common ports, full range, specific ports)</li>
  <li>View detailed IP information</li>
  <li>Exit the program</li>
</ul>

<hr style="border:1px solid #eee;" />

<h2 style="color:#2E86C1;">Requirements</h2>

<ul style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size:1rem; line-height:1.6;">
  <li>Python 3.x</li>
  <li>Built-in Python modules (<code>socket</code>, <code>json</code>, <code>urllib</code>)</li>
  <li>Internet connection for IP info lookup</li>
</ul>

<hr style="border:1px solid #eee;" />

<h2 style="color:#2E86C1;">Important Notes</h2>

<ul style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size:1rem; line-height:1.6;">
  <li>Ensure Python 3 is installed and accessible via <code>python3</code> command.</li>
  <li>Run this tool only on networks and systems you have permission to scan. Unauthorized scanning is illegal and unethical.</li>
  <li>For best results, use a reliable internet connection.</li>
</ul>

<hr style="border:1px solid #eee;" />

<h2 style="color:#2E86C1;">License</h2>

<p style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">This project is licensed under the MIT License.</p>

<hr style="border:1px solid #eee;" />

<h2 style="color:#2E86C1;">Contact</h2>

<p style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
For questions or support, please open an issue on the GitHub repository:<br />
<a href="https://github.com/amirebog/pixelscanner" target="_blank" rel="noopener noreferrer" style="color:#2980B9;">https://github.com/amirebog/pixelscanner</a>
</p>

<hr style="border:1px solid #eee;" />

<p style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-weight:bold;">Thank you for using PixelScanner!</p>
