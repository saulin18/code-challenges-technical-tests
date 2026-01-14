import { userRoles } from "./constants";

export const WILDCARDS = {
    "all": /^.*$/,           // Everything
    "read": /^(list|retrieve|get|read)$/,  // Read actions
    "write": /^(create|update|delete|add|remove|modify|partial-update)$/, // Write actions
    "some": /^some$/,        // Placeholder (no real match)
} as const;


/**
 * Compares a permission query with a permission using wildcards
 * @param query - The permission query to be checked (e.g: "tasks::create::all")
 * @param perm - The user's permission (e.g: "tasks::write::all")
 * @param strict - If true, "some" does not match. If false, "some" matches anything
 */
export function match(
    query: string, 
    perm: string, 
    strict: boolean = true
): boolean | null {
    const queryChunks = query.split("::");
    const permChunks = perm.split("::");
    
    // Debe tener exactamente 3 partes: resource::action::owner
    if (queryChunks.length !== 3 || permChunks.length !== 3) {
        return null; // Invalid format
    }
    
    // Compare each part
    for (let i = 0; i < 3; i++) {
        const queryChunk = queryChunks[i];
        const permChunk = permChunks[i];
        
        // If the permission has a wildcard, check if it matches
        if (permChunk in WILDCARDS) {
            const regex = WILDCARDS[permChunk as keyof typeof WILDCARDS];
            if (!regex.test(queryChunk)) {
                return false; // No matches
            }
        } 
        // If it's not a wildcard and not strict, "some" matches anything
        else if (!strict && queryChunk === "some") {
            continue; // Matches
        }
        // Exact comparison
        else if (queryChunk !== permChunk) {
            return false; // No matches
        }
    }
    
    return true; // All parts match
}

/**
 * Checks if any of the user's permissions match the query
 */
export function matchAny(
    query: string, 
    perms: string[], 
    strict: boolean = true
): boolean {
    return perms.some((perm) => match(query, perm, strict) === true);
}


export interface PermissionContext {
    resource: string;      // Resource (e.g: "tasks", "users", etc.)
    action: string;        // Action (e.g: "create", "read", "update", "delete")
    owner?: string;        // Owner ID (e.g: "123")
    subowner?: string;     // Optional subowner ID (e.g: "456")
}

/**
 * Generates a permission query from a context
 */
export function generatePermissionQuery(context: PermissionContext): string {
    const owner = context.owner ? `owner:${context.owner}` : "some";
    return `${context.resource}::${context.action}::${owner}`;
}

