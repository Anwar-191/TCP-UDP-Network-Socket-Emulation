
# PySocket: TCP & UDP Protocol Implementation

This repository contains Python scripts designed to illustrate the practical, low-level workings of the **TCP (Transmission Control Protocol)** and **UDP (User Datagram Protocol)**[cite: 8, 11]. 

By utilizing Python's built-in networking libraries, this project demonstrates how applications establish client-server communication, handle concurrent connections, and process data payloads across different transport layer protocols[cite: 7, 9, 10].

## 🚀 Features

*   **Multi-threaded TCP Server:** Binds to localhost (port 5050) and utilizes Python's `threading` module to accept and handle multiple client connections simultaneously[cite: 9].
*   **UDP Server:** Binds to localhost (port 5051) and processes connectionless datagrams using `SOCK_DGRAM`[cite: 10].
*   **Interactive Client:** A dynamic client script that prompts the user to select their desired protocol (TCP or UDP) and maintains a communication loop[cite: 7].
*   **Custom Message Protocol:** Processes incoming string payloads based on predefined rules (e.g., sorting characters in descending/ascending order or converting to uppercase)[cite: 8, 9, 10].
*   **Standard Libraries Only:** Built entirely using Python's standard `socket` and `threading` libraries without relying on third-party dependencies[cite: 9, 10, 11].

## 📂 Repository Contents

*   `tcp_server.py`: The primary TCP server script handling multi-threaded connections[cite: 9].
*   `udp_server.py`: The connectionless UDP server script[cite: 10].
*   `client.py`: The interactive client application for dispatching payloads[cite: 7].
*   `Lab2.pdf`: A comprehensive laboratory report detailing the code's logic, execution steps, and verification screenshots[cite: 8, 11].

## 🦈 Network Traffic Analysis (Wireshark)

To demonstrate a deeper understanding of the underlying network protocols, network traffic was captured and analyzed (detailed in `Lab2.pdf`)[cite: 8, 11]. Reviewing the traffic reveals the following network behaviors:

*   **TCP Connection (Port 5050):** Displays the initial TCP 3-way handshake (SYN, SYN-ACK, ACK) required to establish a session before any application data is sent[cite: 8].
*   **TCP Data Transmission:** Highlights the use of `PSH, ACK` flags when the client pushes the string payloads (e.g., `Aebcad`) to the server, and the subsequent acknowledgment[cite: 8].
*   **UDP Connectionless Traffic (Port 5051):** Demonstrates stateless communication where a full transaction consists of only two datagrams (one request, one response) without any prior session establishment[cite: 8].

## 🛠️ Prerequisites

Since this script utilizes standard libraries, no external pip packages are required[cite: 11]. You just need:
*   Python 3.x installed on your system[cite: 11].
*   An active local environment to run loopback connections[cite: 9].

## 💻 Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/anwar-khairy/PySocket-Protocol-Lab.git](https://github.com/anwar-khairy/PySocket-Protocol-Lab.git)
    cd PySocket-Protocol-Lab
    ```

2.  **Start the Servers:**
    Open two separate terminal windows to run both servers simultaneously.
    ```bash
    # In Terminal 1
    python tcp_server.py
    
    # In Terminal 2
    python udp_server.py
    ```

3.  **Execute the client:**
    Open a third terminal window to start the client.
    ```bash
    python client.py
    ```
    *   Enter `TCP` or `UDP` when prompted[cite: 7].
    *   Type a string starting with A, C, or D to test the server's processing rules[cite: 7].
    *   Type `quit` to cleanly exit[cite: 7].
