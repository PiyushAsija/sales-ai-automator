import { useState } from "react";
import axios from "axios";

function App() {

  const [file, setFile] = useState(null);
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {

    if (!file || !email) {
      setMessage("Please upload a file and enter email.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("email", email);

    try {

      setLoading(true);
      setMessage("Processing sales data...");

      const response = await axios.post("https://sales-ai-automator.onrender.com/upload", formData);  

      setMessage("✅ Summary generated and email sent!");

    } catch (error) {

      console.error(error);
      setMessage("❌ Error generating summary");

    }

    setLoading(false);
  };

  return (

    <div style={{ padding: "40px", fontFamily: "Arial" }}>

      <h1>AI Sales Insight Automator</h1>

      <p>Upload sales CSV and receive an AI generated report.</p>

      <br/>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br/><br/>

      <input
        type="email"
        placeholder="Enter email address"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <br/><br/>

      <button onClick={handleSubmit}>
        Generate Summary
      </button>

      <br/><br/>

      {loading && <p>⏳ Processing...</p>}

      <p>{message}</p>

    </div>
  );
}

export default App;