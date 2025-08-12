import { useState } from "react";
import { useEffect } from "react";
import { handleHash } from "../services/hash";
import SideBar from "../components/SideBar";


function UrlShortener() {
    const [url, setUrl] = useState("");
    const [result, setResult] = useState("");
    const [count, setCount] = useState("");
    const [isCopied, setIsCopied] = useState(false);
    const[error,setError]=useState("")


   useEffect (() => {
        setIsCopied(false)
    } ,[url])

  const handleSubmit = async (url: string, e: React.FormEvent) => {
    e.preventDefault();
    if (url) {
      const data = await handleHash(url);
      if(data.error){
        setError(data.error)
      }
      else{
      const shortUrl = `http://127.0.0.1:8000/${data.result.short_url}`;
      setResult(shortUrl);
      setCount(data.result.clicks);
      setError("")
    }}
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(result)
    setIsCopied(true)
  };

  return (
    <div className="min-h-screen bg-gray-800 flex items-center gap-100 p-4">
        <SideBar />
      <div className="bg-white shadow-md rounded-xl p-8 max-w-md w-full">
        <h1 className="text-2xl font-bold text-center mb-6 text-[#8DD8FF]">URL Shortener</h1>
        <div className="text-red-500">{error?"URL does not Exist":''}</div>
        <form onSubmit={(e) => handleSubmit(url, e)} className="flex flex-col gap-4">
          <label className="text-gray-700 font-medium">
            Enter URL:
            <input
              type="text"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              placeholder="Enter your URL"
              className={`mt-2 w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400 ${error?"border-solid border-red-500":""}`}
            />
          </label> 

          <button
            type="submit"
            className="w-full bg-[#8DD8FF] hover:bg-[#273F4F] cursor-pointer text-white font-semibold py-2 rounded-md "
          >
            Shorten URL
          </button>
        </form>

        {result && (
          <div className="mt-6 bg-gray-100 p-4 rounded-md text-center space-y-2">
            <p className="text-sm text-gray-600">Shortened URL:</p>
            <div className="flex justify-center items-center gap-2">
                {result}
              <button
                onClick={handleCopy} 
                className="bg-[#8DD8FF] hover:bg-[#273F4F] cursor-pointer text-white px-3 py-1 rounded-md text-sm"
              >
                {isCopied? 'Copied': 'Copy'}
              </button>
            </div>
            <p className="text-sm text-gray-700">Clicks: <strong>{count}</strong></p>
          </div>
        )}
      </div>
    </div>
  );
}

export default UrlShortener;
