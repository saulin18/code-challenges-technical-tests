import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { useAuth } from "../hooks/useAuth";
import { Form, FormField, FormItem, FormLabel, FormControl, FormMessage } from "@/common/components/ui/form";
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from "@/common/components/ui/card";
import { Button } from "@/common/components/ui/button";
import { Input } from "@/common/components/ui/input";
import { authService } from "../auth-service";
import { z } from "zod";

const registerSchema = z.object({
    email: z.email("Must be a valid email"),
    password: z.string().min(8, "Password must be at least 8 characters"),
    firstName: z.string().min(1, "First name is required").max(100, "Max length of 100 characters"),
    lastName: z.string().min(1, "Last name is required").max(100, "Max length of 100 characters"),
})

type RegisterFormData = z.infer<typeof registerSchema>;

function RegisterForm() {
    const { register: registerMutation } = useAuth(authService());

    const form = useForm<RegisterFormData>({
        // @ts-expect-error - Zod v4 compatibility issue with @hookform/resolvers
        resolver: zodResolver(registerSchema),
        defaultValues: {
            email: "",
            password: "",
            firstName: "",
            lastName: "",
        },
    })

    const onSubmit = async (data: z.infer<typeof registerSchema>) => {
        await registerMutation.mutateAsync({
            email: data.email,
            password: data.password,
            firstName: data.firstName,
            lastName: data.lastName,
        });
    }

    return (
        <Card className="w-full">
            <CardHeader>
                <CardTitle>Create an account</CardTitle>
                <CardDescription>
                    Enter your information to create a new account
                </CardDescription>
            </CardHeader>
            <Form {...form}>
                <form onSubmit={form.handleSubmit(onSubmit)}>
                    <CardContent className="space-y-4">
                        <FormField
                            control={form.control}
                            name="firstName"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>First Name</FormLabel>
                                    <FormControl>
                                        <Input placeholder="John" {...field} />
                                    </FormControl>
                                    <FormMessage />
                                </FormItem>
                            )}
                        />
                        <FormField
                            control={form.control}
                            name="lastName"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Last Name</FormLabel>
                                    <FormControl>
                                        <Input placeholder="Doe" {...field} />
                                    </FormControl>
                                    <FormMessage />
                                </FormItem>
                            )}
                        />
                        <FormField
                            control={form.control}
                            name="email"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Email</FormLabel>
                                    <FormControl>
                                        <Input type="email" placeholder="john.doe@example.com" {...field} />
                                    </FormControl>
                                    <FormMessage />
                                </FormItem>
                            )}
                        />
                        <FormField
                            control={form.control}
                            name="password"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Password</FormLabel>
                                    <FormControl>
                                        <Input type="password" placeholder="••••••••" {...field} />
                                    </FormControl>
                                    <FormMessage />
                                </FormItem>
                            )}
                        />
                    </CardContent>
                    <CardFooter>
                        <Button 
                            type="submit" 
                            className="w-full"
                            disabled={registerMutation.isPending}
                        >
                            {registerMutation.isPending ? "Creating account..." : "Create account"}
                        </Button>
                    </CardFooter>
                </form>
            </Form>
        </Card>
    )
}

export default RegisterForm