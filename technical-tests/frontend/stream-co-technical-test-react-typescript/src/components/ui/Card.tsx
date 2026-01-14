import React from 'react'
import './card.css'
import clsx from 'clsx'

interface CardProps {
  children: React.ReactNode
  className?: string

}

function Card({ children, className, ...props }: CardProps) {
  return (
    <div {...props} className={clsx(className, "card-container")}>
      { children }
    </div>
  )
}

interface CardTitleProps extends React.HTMLAttributes<HTMLHeadingElement> {
  children: React.ReactNode
  className?: string
}

function CardTitle({ children, className, ...props }: CardTitleProps) {
  return (
    <h2 {...props} className={clsx(className, "card-title")}>
      { children }
    </h2>
  )
}

Card.Title = CardTitle;

interface CardDescriptionProps extends React.HTMLAttributes<HTMLParagraphElement>{
  children?: React.ReactNode
  className?: string
}

function CardDescription({children, className, ...props}  : CardDescriptionProps) {
  return (
    <p {...props} className={clsx(className, "card-description")}>
      { children }
    </p>
  )
}

Card.Description = CardDescription;

interface CardContentProps extends React.HTMLAttributes<HTMLDivElement> {
  children?: React.ReactNode
  className?: string

  backgroundImage?: string
}

function CardContent({children, className, backgroundImage, ...props}  : CardContentProps) {
  return (
    <div {...props} className={clsx(className, "card-content")}>
      { backgroundImage && <img src={backgroundImage} alt="background" className="card-background-image" /> }
      { children }
    </div>
  )
}

Card.Content = CardContent;

export default Card