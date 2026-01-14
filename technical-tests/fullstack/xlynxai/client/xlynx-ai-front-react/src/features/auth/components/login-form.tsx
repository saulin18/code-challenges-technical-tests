import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import * as z from "zod"
import { authService } from '../auth-service'
import { useAuth } from '../hooks/useAuth'
import { Form, FormField, FormItem, FormLabel, FormControl, FormMessage } from '@/common/components/ui/form'
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from '@/common/components/ui/card'
import { Input } from '@/common/components/ui/input'
import { Button } from '@/common/components/ui/button'
import { useNavigate } from 'react-router'

const loginSchema = z.object({
    email: z.string().email("Must be a valid email"),
    password: z.string().min(8, "Password must be at least 8 characters"),
})

type LoginFormData = z.infer<typeof loginSchema>;

function LoginForm() {
    const { login: loginMutation } = useAuth(authService());
    const navigate = useNavigate();
    const form = useForm<LoginFormData>({
        // @ts-expect-error - Zod v4 compatibility issue with @hookform/resolvers
        resolver: zodResolver(loginSchema),
        defaultValues: {
            email: "",
            password: "",
        },
    })

    const onSubmit = async (data: z.infer<typeof loginSchema>) => {
        await loginMutation.mutateAsync({
            email: data.email,
            password: data.password,
        });
        navigate("/tasks");
    }

    return (
        <Card className="w-full">
            <CardHeader>
                <CardTitle>Login</CardTitle>
                <CardDescription>
                    Enter your email and password to login
                </CardDescription>
            </CardHeader>
            <Form {...form}>
                <form onSubmit={form.handleSubmit(onSubmit as any)}>
                    <CardContent className="space-y-4">
                        <FormField control={form.control as any} name="email" render={({ field }) => (
                        <FormItem>
                            <FormLabel>Email</FormLabel>
                            <FormControl>
                                <Input type="email" placeholder="john.doe@example.com" {...field} />
                            </FormControl>
                            <FormMessage />
                        </FormItem>
                    )} />
                        <FormField control={form.control as any} name="password" render={({ field }) => (
                            <FormItem>
                                <FormLabel>Password</FormLabel>
                                <FormControl>
                                    <Input type="password" placeholder="••••••••" {...field} />
                                </FormControl>
                                <FormMessage />
                            </FormItem>
                        )} />
                    </CardContent>
            <CardFooter>
                <Button type="submit" className="w-full" disabled={loginMutation.isPending}>
                    {loginMutation.isPending ? "Logging in..." : "Login"}
                </Button>
            </CardFooter>
                </form>
            </Form>
        </Card>
    )
}

export default LoginForm
