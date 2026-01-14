import { useState } from 'react'
import LoginForm from './components/login-form'
import RegisterForm from './components/register-form'
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/common/components/ui/card'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/common/components/ui/tabs'

export function AuthPage() {
    const [activeTab, setActiveTab] = useState<"login" | "register">("login");

    return (
        <div className="min-h-screen flex items-center justify-center p-4">
            <Card className="w-full max-w-md">
                <CardHeader>
                    <CardTitle>Authentication</CardTitle>
                    <CardDescription>
                        Choose an option to continue
                    </CardDescription>
                </CardHeader>
                <CardContent>
                    <Tabs value={activeTab} onValueChange={(value) => setActiveTab(value as "login" | "register")}>
                        <TabsList className="grid w-full grid-cols-2">
                            <TabsTrigger value="login">Login</TabsTrigger>
                            <TabsTrigger value="register">Register</TabsTrigger>
                        </TabsList>
                        <TabsContent value="login" className="mt-4">
                            <LoginForm />
                        </TabsContent>
                        <TabsContent value="register" className="mt-4">
                            <RegisterForm />
                        </TabsContent>
                    </Tabs>
                </CardContent>
            </Card>
        </div>
    )
}

