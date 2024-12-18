export class Router {
  static async analyzeCode(input: string) {
    try {
      const response = await fetch("http://localhost:8000/code-snippet-analyzer", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code: input, language: "English", model: "GPT" }),
      });

      if (!response.ok) throw new Error("API response error");

      return (await response.json());
    } catch (error) {
      console.error("Error calling the local API:", error);
      throw error;
    }
  }
}
