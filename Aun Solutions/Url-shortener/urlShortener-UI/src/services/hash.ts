export const handleHash = async (url:any) => {
    try {
      const response = await fetch('http://127.0.0.1:8000/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({"long_url":url}),
      });
      const data = await response.json();
      console.log("data is ",data)
      return data
    } catch (error) {
      console.error('Error Hasing:', error);
    }
  };