from CNNclassifier.config.configuration import ConfigurationManager
from CNNclassifier.components.model_evaluation_mlflow import Evaluation
from CNNclassifier import logger

STAGE_NAME = "Evaluation stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        eval = Evaluation(eval_config)
        eval.evaluation()
        eval.save_score()
       # eval.log_into_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        evaluate = EvaluationPipeline()
        evaluate.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

    
        