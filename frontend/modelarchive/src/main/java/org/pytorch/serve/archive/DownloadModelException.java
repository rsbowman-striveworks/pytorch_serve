package org.pytorch.serve.archive;

public class DownloadModelException extends ModelException {

    static final long serialVersionUID = 1L;

    /**
     * Constructs an {@code DownloadModelException} with the specified detail message.
     *
     * @param message The detail message (which is saved for later retrieval by the {@link
     *     #getMessage()} method)
     */
    public DownloadModelException(String message) {
        super(message);
    }

    /**
     * Constructs an {@code DownloadModelException} with the specified detail message and cause.
     *
     * <p>Note that the detail message associated with {@code cause} is <i>not</i> automatically
     * incorporated into this exception's detail message.
     *
     * @param message The detail message (which is saved for later retrieval by the {@link
     *     #getMessage()} method)
     * @param cause The cause (which is saved for later retrieval by the {@link #getCause()}
     *     method). (A null value is permitted, and indicates that the cause is nonexistent or
     *     unknown.)
     */
    public DownloadModelException(String message, Throwable cause) {
        super(message, cause);
    }
}
