using UnityEngine;
using System.Net.Sockets;
using System.Text;
using System.Threading;

public class AvatarEmotionController : MonoBehaviour
{
    private TcpListener listener;
    private Thread listenerThread;
    private TcpClient connectedClient;
    private Animator avatarAnimator;

    void Start()
    {
        avatarAnimator = GetComponent<Animator>();
        listenerThread = new Thread(new ThreadStart(ListenForData));
        listenerThread.IsBackground = true;
        listenerThread.Start();
    }

    void ListenForData()
    {
        try
        {
            listener = new TcpListener(System.Net.IPAddress.Any, 65432);
            listener.Start();
            Debug.Log("Listening for connections...");

            while (true)
            {
                connectedClient = listener.AcceptTcpClient();
                NetworkStream stream = connectedClient.GetStream();

                byte[] buffer = new byte[1024];
                int bytesRead = stream.Read(buffer, 0, buffer.Length);
                string receivedData = Encoding.UTF8.GetString(buffer, 0, bytesRead);

                ProcessReceivedData(receivedData);
            }
        }
        catch (SocketException socketException)
        {
            Debug.Log("SocketException " + socketException.ToString());
        }
    }

    void ProcessReceivedData(string data)
    {
        // Parse the received data
        var emotionData = JsonUtility.FromJson<EmotionData>(data);

        // Update the avatar based on the emotion received
        switch (emotionData.emotion.ToLower())
        {
            case "happy":
                avatarAnimator.SetTrigger("Happy");
                break;
            case "sad":
                avatarAnimator.SetTrigger("Sad");
                break;
            case "angry":
                avatarAnimator.SetTrigger("Angry");
                break;
            // Add more cases as needed for different emotions
        }
    }

    private void OnApplicationQuit()
    {
        listener.Stop();
        connectedClient.Close();
    }

    // Define a class to match the JSON structure
    [System.Serializable]
    public class EmotionData
    {
        public string emotion;
    }
}
