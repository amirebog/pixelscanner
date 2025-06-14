#!/bin/bash

clear
echo -e "\e[36m"
echo "██████╗ ██╗██╗     ███████╗██╗  ██╗███████╗ █████╗ ██╗   ██╗███████╗███╗   ██╗"
echo "██╔══██╗██║██║     ██╔════╝██║ ██╔╝██╔════╝██╔══██╗██║   ██║██╔════╝████╗  ██║"
echo "██████╔╝██║██║     █████╗  █████╔╝ █████╗  ███████║██║   ██║█████╗  ██╔██╗ ██║"
echo "██╔═══╝ ██║██║     ██╔══╝  ██╔═██╗ ██╔══╝  ██╔══██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║"
echo "██║     ██║███████╗███████╗██║  ██╗███████╗██║  ██║ ╚████╔╝ ███████╗██║ ╚████║"
echo "╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝"
echo -e "                            \e[0mby Pixel Haven Dev\n"

sleep 1

download_with_progress() {
    url=$1
    output=$2
    echo -e "\e[33mDownloading $output...\e[0m"
    # curl با نوار پیشرفت داخلی (-#)
    curl -# -L "$url" -o "$output"
}

if ! command -v curl &> /dev/null
then
    echo -e "\e[31mcurl not found. Installing curl...\e[0m"
    pkg update -y
    pkg install -y curl
else
    echo -e "\e[32mcurl is installed.\e[0m"
fi


if ! command -v python3 &> /dev/null
then
    echo -e "\e[31mpython3 not found. Installing python3...\e[0m"
    pkg update -y
    pkg install -y python
else
    echo -e "\e[32mpython3 is installed.\e[0m"
fi

SCRIPT_NAME="pixelscanner.py"
SCRIPT_URL="https://raw.githubusercontent.com/amirebog/pixelscanner/refs/heads/main/pixelscanner.py"

download_with_progress "$SCRIPT_URL" "$SCRIPT_NAME"

chmod +x "$SCRIPT_NAME"

echo -e "\n\e[32mInstallation complete!\e[0m"
echo -e "Run the scanner with this command:"
echo -e "\e[36mpython3 $SCRIPT_NAME\e[0m"
echo -e "\nThank you for using Pixel Haven Dev tools!"

exit 0
