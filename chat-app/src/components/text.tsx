import * as React from "react";
import styles from './text.module.css';  // Importando o arquivo CSS

export interface TextareaProps extends React.TextareaHTMLAttributes<HTMLTextAreaElement> {}

const Text = React.forwardRef<HTMLTextAreaElement, TextareaProps>(
  ({ className, ...props }, ref) => {
    return (
      <div className={styles.textareaWrapper}>
        <textarea
          className={`${styles.textarea} ${className}`}
          ref={ref}
          {...props}
        />
      </div>
    );
  }
);

Text.displayName = "Textarea";

export { Text };
