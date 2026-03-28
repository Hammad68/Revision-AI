import express from 'express';
import OpenAI from 'openai';
import dotenv from 'dotenv';
dotenv.config();

const app = express();
const port = 3000;

// 1. Initialize the DeepSeek client
const openai = new OpenAI({
  baseURL: 'https://api.deepseek.com',
  apiKey: process.env.DEEPSEEK_API_KEY, // Ensure this matches your .env file
});

app.get('/test-deepseek', async (req, res) => {
  try {
    // 2. Make a simple test request
    const response = await openai.chat.completions.create({
      model: "deepseek-chat",
      messages: [
        { role: "system", content: "You are a helpful assistant." },
        { role: "user", content: "Hello! Is this API working?" },
      ],
      stream: false,
    });

    // 3. Return the result
    res.json({
      success: true,
      message: response.choices[0].message.content,
    });
  } catch (error) {
    console.error("DeepSeek API Error:", error);
    res.status(500).json({
      success: false,
      error: error.message,
    });
  }
});

app.listen(port, () => {
  console.log(`Test server running at http://localhost:${port}/test-deepseek`);
});
