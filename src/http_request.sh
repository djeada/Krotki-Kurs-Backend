#!/bin/bash

# Check if a URL was provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <url>"
  exit 1
fi

# Parse the URL
url="$1"
protocol=$(echo $url | sed -e's,^\(.*://\).*,\1,g')
url_no_protocol=$(echo $url | sed -e's,^\(.*://\)\(.*\),\2,g')
host_port_path=$(echo $url_no_protocol | cut -d/ -f1)
path=$(echo $url_no_protocol | grep / | cut -d/ -f2-)
path="/${path}"
host=$(echo $host_port_path | sed -e 's,:.*,,g')
port=$(echo $host_port_path | grep : | cut -d: -f2)
port=${port:-80}

# Open the TCP connection to the host on the specified port
exec 3<>/dev/tcp/$host/$port

# Define the HTTP request
lines=(
  "GET $path HTTP/1.1"
  "Host: $host"
  "Connection: close"
  ""
)

# Send the HTTP request
printf '%s\r\n' "${lines[@]}" >&3

# Read and display the server response
while read -r data <&3; do
  echo "got server data: $data"
done

# Close the TCP connection
exec 3>&-
