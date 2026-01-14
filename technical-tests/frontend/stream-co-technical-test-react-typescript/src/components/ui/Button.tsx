import React, { Children } from 'react'
import './button.css';
import clsx from 'clsx';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement>  {

    label: string;
    onClick: () => void;
    className?: string;

    variant: "primary" | "secondary" | "transparent"
}

const variantClasses = {
   primary: 'primary',
   secondary: 'secondary',
   transparent: 'transparent',
}    

const Button = ({ children, onClick, className, variant, ...props }: ButtonProps) => {
    return (
        <button className={clsx(className, variantClasses[variant])} onClick={onClick} {...props}>
            {children}
        </button>
    )
}

export default Button