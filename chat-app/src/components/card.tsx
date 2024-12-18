import styles from './card.module.css';

interface MessageCardProps {
  role: string;
  content: string;
}

const MessageCard = ({ role, content }: MessageCardProps) => {
  const cardStyle = role === 'user' ? styles.user : styles.bot;

  return (
    <div className={`${styles.card} ${cardStyle}`}>
      <p className={styles.messageContent}>{content}</p>
    </div>
  );
};

export default MessageCard;
