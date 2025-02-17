using Xunit;
using System;

public class ProgramTests
{
    [Fact]
    public void GetLanguage_WithNullInput_ShouldThrowArgumentNullException()
    {
        // Arrange
        string text = null;

        // Act & Assert
        Assert.Throws<ArgumentNullException>(() => Program.GetLanguage(text));
    }

    [Fact]
    public void GetLanguage_WithEmptyStringInput_ShouldReturnUnknown()
    {
        // Arrange
        string text = "";

        // Act
        string result = Program.GetLanguage(text);

        // Assert
        Assert.Equal("Unknown", result);
    }

    [Fact]
    public void GetLanguage_WithInvalidDataTypeInput_ShouldThrowArgumentException()
    {
        // Arrange
        object invalidInput = 123;

        // Act & Assert
        Assert.Throws<ArgumentException>(() => Program.GetLanguage((string)invalidInput));
    }
}