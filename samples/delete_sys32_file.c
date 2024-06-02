#include <stdio.h>
#include <windows.h>

int main() {
    // Path to the file you want to delete
    const char *filePath = "C:\\Windows\\System32\\adsldp_cp.dll"; // Replace with the actual file you want to delete

    // Attempt to delete the file
    if (DeleteFile(filePath)) {
        printf("File deleted successfully.\n");
    } else {
        // If the file deletion fails, get the error code
        DWORD error = GetLastError();
        printf("Failefd to delete the file. Error code: %lu\n", error);
    }

    return 0;
}
