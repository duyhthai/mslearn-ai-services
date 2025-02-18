using NUnit.Framework;
using System;

[TestFixture]
public class ProgramTests
{
    [Test]
    public void GetLanguage_InvalidTextType_ThrowsArgumentException()
    {
        // Arrange
        string aiSvcKey = "your_ai_svc_key";
        string aiSvcEndpoint = "your_ai_svc_endpoint";
        object invalidText = new object();

        // Act & Assert
        Assert.Throws<ArgumentException>(() => Program.GetLanguage(invalidText.ToString()));
    }

    [Test]
    public void GetLanguage_EmptyText_ReturnsNull()
    {
        // Arrange
        string aiSvcKey = "your_ai_svc_key";
        string aiSvcEndpoint = "your_ai_svc_endpoint";
        string emptyText = "";

        // Act
        string result = Program.GetLanguage(emptyText);

        // Assert
        Assert.IsNull(result);
    }

    [Test]
    public void GetLanguage_NullText_ThrowsArgumentNullException()
    {
        // Arrange
        string aiSvcKey = "your_ai_svc_key";
        string aiSvcEndpoint = "your_ai_svc_endpoint";
        string nullText = null;

        // Act & Assert
        Assert.Throws<ArgumentNullException>(() => Program.GetLanguage(nullText));
    }
}