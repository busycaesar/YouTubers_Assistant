from langchain.prompts import PromptTemplate
from .llm import generate_response
from .youtube import get_video_transcript

def get_keywords_suggestions(video_link, gemini_api_keys):
    # Get the transcript of the video.
    video_transcript = get_video_transcript(video_link)

    # Initiate a prompt template.
    prompt_template = PromptTemplate(
        input_variables=["video_transcript"],
        template="""
        Given the following transcript of a video, generate 5 catchy and SEO-friendly hashtags that are relevant to the video content. Please ensure the hashtags are high-performing for SEO optimization and are aligned with the topic of the video.

        Video Transcript: {video_transcript}
        """
        )

    # Call the function to generate the response by passing the prompt template and input variables.
    generated_response = generate_response(
            prompt_template, 
            { "video_transcript": video_transcript },
            gemini_api_keys
        )
    
    # Return the generated response.
    return generated_response