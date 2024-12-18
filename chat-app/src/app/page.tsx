"use client";
import MessageCard from "@/components/card";
import { Text } from "@/components/text";
import { useRef, useState, useEffect } from "react";
import { Router } from "@/services/router";
import styles from "./styles.module.css";

interface MessageType {
  id: string;
  role: string;
  content: string;
}

export default function Home() {
  const [messages, setMessages] = useState<MessageType[]>([]);
  const [input, setInput] = useState<string>("");
  const [isLoading, setIsLoading] = useState<boolean>(false); // Estado para controle de carregamento
  const formRef = useRef<HTMLFormElement>(null);

  const generateUniqueId = () => `${Date.now()}-${Math.random().toString(36).substring(2, 15)}`;
  
  useEffect(() => {
    const initialMessage = { 
      id: generateUniqueId(), 
      role: "bot", 
      content: "Hey! How’s it going? 😊 I’m Anne, and I’m super excited to meet you! If you’ve got any code you’d like me to take a look at, just send it over. I’m here to help! Let’s dive in and have some fun with it! 😉"
    };
  
    const initialMessageExplain = { 
      id: generateUniqueId(), 
      role: "bot", 
      content: `Alright, I’m about to take a look at your code. Here’s what you can expect:
      1. A quick explanation of what your code is doing.
      2. Some suggestions to make it cleaner and more efficient.
      3. A breakdown of the changes—I’ll walk you through what I did and why it works better.
      Let’s get started and see how we can make your code even better!`
    };
  
    setMessages([initialMessage, initialMessageExplain]);
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    setInput('');
    setIsLoading(true); 
    e.preventDefault();

    const userMessage = { id: generateUniqueId(), role: "user", content: input };
    setMessages((prevMessages) => [...prevMessages, userMessage]);

    try {
      const data = await Router.analyzeCode(input);

      const botMessages = [
        { id: generateUniqueId(), role: "bot", content: data.explanation },
        { id: generateUniqueId(), role: "bot", content: data.refactored_code },
        { id: generateUniqueId(), role: "bot", content: data.explanation_of_refactor },
      ];

      setMessages((prevMessages) => [...prevMessages, ...botMessages]);
    } catch (error) {
      console.error("Error processing the request:", error);
    } finally {
      setIsLoading(false); 
    }
  };

  return (
    <main className={styles.mainContainer}>
      <div className={styles.messagesContainer}>
        {messages.map((message) => (
          <MessageCard key={message.id} role={message.role} content={message.content} />
        ))}
        {isLoading && (
          <div className={styles.loadingCard}>
            <MessageCard key="loading" role="bot" content="Just a moment, I'm analyzing the language and jotting down some improvements for your code..." />
          </div>
        )}
      </div>

      <form ref={formRef} onSubmit={handleSubmit} className={styles.formContainer}>
        <Text
          className={styles.textInput}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && !e.shiftKey && formRef.current?.requestSubmit()}
        />
      </form>
    </main>
  );
}
