export interface Room {
  room_id: string;
  user: User;
  messages: Message[] | null;
}

export interface Message {
  message_id: string;
  sender_id: string;
  message: string;
  professional: Professional;
  patient: Professional;
  sent_at: string;
}

export interface Professional {
  user_id: string;
  name: string;
}

export interface User {
  user_id: string;
  name: string;
  avatar: string;
}
