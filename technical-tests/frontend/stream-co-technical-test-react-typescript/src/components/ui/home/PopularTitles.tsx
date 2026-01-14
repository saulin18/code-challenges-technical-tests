
import './home.css'
import clsx from 'clsx'

interface PopularBannerProps {
   children: React.ReactNode
   className?: string
}   

function PopularBanner({ children, className, ...props }: PopularBannerProps) {
  return (
     <div className={clsx('popular-titles-container', className)}>
        <h2 {...props} className='popular-titles-title'>
            {children}
        </h2>
     </div>
  )
}

export default PopularBanner